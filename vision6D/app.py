from typing import List, Dict, Tuple
import pathlib
import logging
import numpy as np
from PIL import Image
import copy
import math
import functools

import pyvista as pv
import trimesh
import cv2
from easydict import EasyDict
import matplotlib.pyplot as plt

from . import utils

logger = logging.getLogger("vision6D")

class App:

    def __init__(
            self, 
            register,
            width: int=1920,
            height: int=1080,
            scale: float=1,
            # use surgical microscope for medical device with view angle 1 degree
            cam_focal_length:int=5e+4,
            cam_viewup: Tuple=(0,-1,0),
        ):
        
        self.window_size = (int(width*scale), int(height*scale))
        self.scale = scale
        self.reference = None
        self.transformation_matrix = None
        
        self.image_actors = {}
        self.mesh_actors = {}
        
        self.image_polydata = {}
        self.mesh_polydata = {}
        
        self.binded_meshes = {}
        
        # default opacity for image and surface
        self.set_image_opacity(0.999) # self.image_opacity = 0.35
        self.set_surface_opacity(0.999) # self.surface_opacity = 1

        # Set up the camera
        self.camera = pv.Camera()

        # Set camera intrinsic attribute
        self.camera_intrinsics = np.array([
            [cam_focal_length, 0, width/2],
            [0, cam_focal_length, height/2],
            [0, 0, 1]
        ])
        self.original_camera_intrinsics = copy.deepcopy(self.camera_intrinsics)
        self.cam_viewup = cam_viewup
        self.set_camera_intrinsics(self.camera_intrinsics)
        self.set_camera_extrinsics()
        
        # Set the attribute and its implications
        self.set_register(register)
        
        # render image and ossicles
        self.pv_render = pv.Plotter(window_size=[self.window_size[0], self.window_size[1]], lighting=None, off_screen=True)
        self.pv_render.store_image = True
        
    def set_register(self, register: bool):
        # plot image and ossicles
        self.register = register
        
        if self.register:
            self.pv_plotter = pv.Plotter(window_size=[self.window_size[0], self.window_size[1]])
        else:
            self.pv_plotter = pv.Plotter(window_size=[self.window_size[0], self.window_size[1]], off_screen=True)
            self.pv_plotter.store_image = True
    
    def set_image_opacity(self, image_opacity: float):
        self.image_opacity = image_opacity
    
    def set_surface_opacity(self, surface_opacity: float):
        self.surface_opacity = surface_opacity

    def set_camera_extrinsics(self):
        # self.camera.SetPosition((0,0,-(self.cam_focal_length/100)/self.scale))
        self.camera.SetPosition((0,0,-(self.camera_intrinsics[0,0]/100)/self.scale))
        self.camera.SetFocalPoint((0,0,0))
        self.camera.SetViewUp(self.cam_viewup)
    
    def set_camera_intrinsics(self, camera_intrinsics):

        width = self.window_size[0]
        height = self.window_size[1]
        
        cx = camera_intrinsics[0,2]
        cy = camera_intrinsics[1,2]
        f = camera_intrinsics[0,0]
        
        # convert the principal point to window center (normalized coordinate system) and set it
        wcx = -2*(cx - float(width)/2) / width
        wcy =  2*(cy - float(height)/2) / height
        self.camera.SetWindowCenter(wcx, wcy) # (0,0)
        
        # Setting the focal length
        view_angle = 180 / math.pi * (2.0 * math.atan2(height/2.0, f))
        self.camera.SetViewAngle(view_angle) # ~30 degree
        
    def set_transformation_matrix(self, matrix:np.ndarray):
        self.transformation_matrix = matrix
    
    def set_reference(self, name:str):
        self.reference = name
        
    def set_vertices(self, name:str, vertices: pv.pyvista_ndarray):
        if vertices.shape[0] == 3: 
            setattr(self, f"{name}_vertices", vertices)
        elif vertices.shape[1] == 3: 
            setattr(self, f"{name}_vertices", vertices.T)
        
    # Suitable for total two and above mesh quantities
    def bind_meshes(self, main_mesh: str, key: str):
        
        other_meshes = []
    
        for mesh_name in self.mesh_polydata.keys():
                if mesh_name != main_mesh:
                    other_meshes.append(mesh_name)
            
        self.binded_meshes[main_mesh] = {'key': key, 'meshes': other_meshes}
        
    def load_image(self, image_source, scale_factor:list=[0.01,0.01,1]):
        
        if isinstance(image_source, pathlib.Path):
            self.image_polydata['image'] = pv.get_reader(image_source).read()
            self.image_polydata['image'] = self.image_polydata['image'].scale(scale_factor, inplace=False)
            
        elif isinstance(image_source, np.ndarray):
            self.image_polydata['image'] = pv.UniformGrid(dimensions=(1920, 1080, 1), spacing=(0.01, 0.01, 1), origin=(0.0, 0.0, 0.0))
            self.image_polydata['image'].point_data["values"] = image_source.reshape((1920*1080, 3)) # order = 'C

        self.image_polydata['image'] = self.image_polydata['image'].translate(-1 * np.array(self.image_polydata['image'].center), inplace=False)
        self.image_polydata["image-origin"] = self.image_polydata['image'].copy()
            
        # Then add it to the plotter
        image = self.pv_plotter.add_mesh(self.image_polydata['image'], rgb=True, opacity=self.image_opacity, name='image')
        actor, _ = self.pv_plotter.add_actor(image, name="image")

        # Save actor for later
        self.image_actors["image"] = actor
        self.image_actors["image-origin"] = actor.copy()

    def load_meshes(self, paths: Dict[str, (pathlib.Path or pv.PolyData)]):
        
        reference_name = None
        
        if self.transformation_matrix is None:
           raise RuntimeError("Transformation matrix is not set")
        
        for mesh_name, mesh_source in paths.items():
            
            reference_name = mesh_name

            if isinstance(mesh_source, pathlib.WindowsPath):
                # Load the mesh
                if '.ply' in str(mesh_source):
                    mesh_data = pv.get_reader(mesh_source).read()
                elif '.mesh' in str(mesh_source):
                    mesh_data = pv.wrap(utils.load_trimesh(mesh_source))
            elif isinstance(mesh_source, pv.PolyData):
                mesh_data = mesh_source
                
            self.mesh_polydata[mesh_name] = mesh_data
            
            self.set_vertices(mesh_name, mesh_data.points)
            
            # Apply transformation to the mesh vertices
            transformed_points = utils.transform_vertices(self.transformation_matrix, mesh_data.points)
            
            assert (mesh_data.points == transformed_points).all(), "they should be identical!"
            
            colors = utils.color_mesh(transformed_points.T)
            
            # Color the vertex
            mesh_data.point_data.set_scalars(colors)

            mesh = self.pv_plotter.add_mesh(mesh_data, rgb=True, opacity = self.surface_opacity, name=mesh_name)
            
            mesh.user_matrix = self.transformation_matrix
            
            actor, _ = self.pv_plotter.add_actor(mesh, name=mesh_name)
            
            # Save actor for later
            self.mesh_actors[mesh_name] = actor
            
            # logger.debug(f"\n{mesh_name} orientation: {self.mesh_actors[mesh_name].orientation}")
            # logger.debug(f"\n{mesh_name} position: {self.mesh_actors[mesh_name].position}")
            
        if len(self.mesh_actors) == 1:
            self.set_reference(reference_name)
            
    def event_zoom_out(self, *args):
        logger.debug(f"before event_zoom_out callback, camera view angle: {self.pv_plotter.camera.view_angle}")

        # self.pv_plotter.camera.zoom(0.5)

        self.camera_intrinsics[0,0]/=2
        self.set_camera_intrinsics(self.camera_intrinsics)
        self.pv_plotter.camera = self.camera.copy()

        logger.debug(f"after event_zoom_out callback complete, camera view angle: {self.pv_plotter.camera.view_angle}")
        print("hhh")

    def event_zoom_in(self, *args):
        logger.debug(f"before event_zoom_out callback, camera view angle: {self.pv_plotter.camera.view_angle}")

        # self.pv_plotter.camera.zoom(2)

        self.camera_intrinsics[0,0]*= 2
        self.set_camera_intrinsics(self.camera_intrinsics)
        self.pv_plotter.camera = self.camera.copy()
        logger.debug(f"after event_zoom_in callback complete, camera view angle: {self.pv_plotter.camera.view_angle}")
        print("hhh")

    def event_reset_camera(self, *args):
        self.camera_intrinsics = self.original_camera_intrinsics
        self.set_camera_intrinsics(self.camera_intrinsics)
        self.pv_plotter.camera = self.camera.copy()

        logger.debug("reset_camera_event callback complete")

    def event_reset_image(self, *args):
        self.image_actors["image"] = self.image_actors["image-origin"].copy() # have to use deepcopy to prevent change self.image_actors["image-origin"] content
        self.pv_plotter.add_actor(self.image_actors["image"], name="image")
        logger.debug("reset_image_position callback complete")
        
    def event_toggle_image_opacity(self, *args, up):
        if up:
            self.image_opacity += 0.2
            if self.image_opacity >= 1:
                self.image_opacity = 1
        else:
            self.image_opacity -= 0.2
            if self.image_opacity <= 0:
                self.image_opacity = 0
        
        self.image_actors["image"].GetProperty().opacity = self.image_opacity
        self.pv_plotter.add_actor(self.image_actors["image"], name="image")

        logger.debug("event_toggle_image_opacity callback complete")
        
    def event_toggle_surface_opacity(self, *args, up):    
        if up:
            self.surface_opacity += 0.2
            if self.surface_opacity > 1:
                self.surface_opacity = 1
        else:
            self.surface_opacity -= 0.2
            if self.surface_opacity < 0:
                self.surface_opacity = 0
                
        transformation_matrix = self.mesh_actors[self.reference].user_matrix
        for actor_name, actor in self.mesh_actors.items():
            actor.user_matrix = transformation_matrix
            actor.GetProperty().opacity = self.surface_opacity
            self.pv_plotter.add_actor(actor, name=actor_name)

        logger.debug("event_toggle_surface_opacity callback complete")
        
    def event_track_registration(self, *args):
        
        transformation_matrix = self.mesh_actors[self.reference].user_matrix
        for actor_name, actor in self.mesh_actors.items():
            actor.user_matrix = transformation_matrix
            self.pv_plotter.add_actor(actor, name=actor_name)
            logger.debug(f"<Actor {actor_name}> RT: \n{actor.user_matrix}")
    
    def event_realign_meshes(self, *args, main_mesh=None, other_meshes=[]):
        
        objs = {'fix' : main_mesh,
                'move': other_meshes}
        
        transformation_matrix = self.mesh_actors[f"{objs['fix']}"].user_matrix
        
        for obj in objs['move']:
            self.mesh_actors[f"{obj}"].user_matrix = transformation_matrix
            self.pv_plotter.add_actor(self.mesh_actors[f"{obj}"], name=obj)
        
        logger.debug(f"realign: main => {main_mesh}, others => {other_meshes} complete")
        
    def event_gt_position(self, *args):
        
        for actor_name, actor in self.mesh_actors.items():
            actor.user_matrix = self.transformation_matrix
            self.pv_plotter.add_actor(actor, name=actor_name)

        logger.debug(f"\ncurrent gt rt: \n{self.transformation_matrix}")
        logger.debug("event_gt_position callback complete")
        
    def event_change_gt_position(self, *args):
        self.transformation_matrix = self.mesh_actors[self.reference].user_matrix
        for actor_name, actor in self.mesh_actors.items():
            actor.user_matrix = self.transformation_matrix
            self.pv_plotter.add_actor(actor, name=actor_name)
        
        logger.debug(f"\ncurrent gt rt: \n{self.transformation_matrix}")
        logger.debug("event_change_gt_position callback complete")
    
    def plot(self):
        
        if self.reference is None:
           raise RuntimeError("reference name is not set")

        self.pv_plotter.enable_joystick_actor_style()
        self.pv_plotter.enable_trackball_actor_style()

        # Register callbacks
        self.pv_plotter.add_key_event('c', self.event_reset_camera)
        self.pv_plotter.add_key_event('z', self.event_zoom_out)
        self.pv_plotter.add_key_event('x', self.event_zoom_in)
        self.pv_plotter.add_key_event('d', self.event_reset_image)
        self.pv_plotter.add_key_event('t', self.event_track_registration)

        for main_mesh, mesh_data in self.binded_meshes.items():
            event_func = functools.partial(self.event_realign_meshes, main_mesh=main_mesh, other_meshes=mesh_data['meshes'])
            self.pv_plotter.add_key_event(mesh_data['key'], event_func)
        
        self.pv_plotter.add_key_event('k', self.event_gt_position)
        self.pv_plotter.add_key_event('l', self.event_change_gt_position)
        
        event_toggle_image_opacity_up_func = functools.partial(self.event_toggle_image_opacity, up=True)
        self.pv_plotter.add_key_event('v', event_toggle_image_opacity_up_func)
        event_toggle_image_opacity_down_func = functools.partial(self.event_toggle_image_opacity, up=False)
        self.pv_plotter.add_key_event('b', event_toggle_image_opacity_down_func)
        
        event_toggle_surface_opacity_up_func = functools.partial(self.event_toggle_surface_opacity, up=True)
        self.pv_plotter.add_key_event('y', event_toggle_surface_opacity_up_func)
        event_toggle_surface_opacity_up_func = functools.partial(self.event_toggle_surface_opacity, up=False)
        self.pv_plotter.add_key_event('u', event_toggle_surface_opacity_up_func)
        
        # Set the camera initial parameters
        self.pv_plotter.camera = self.camera.copy()
        
        if self.register:
            self.pv_plotter.add_axes()
            # add the camera orientation to move the camera
            _ = self.pv_plotter.add_camera_orientation_widget()
            # Actual presenting
            cpos = self.pv_plotter.show(title="vision6D", return_cpos=True) # cpos: [(0.0, 0.0, -500.0), (0.0, 0.0, 0.0), (0.0, -1.0, 0.0)]
            print("hhhh")
        else:
            self.pv_plotter.disable()
            self.pv_plotter.show(title="vision6D")
            last_image = self.pv_plotter.last_image
            return last_image
        
    def render_scene(self, scene_source, render_image:bool, scale_factor:Tuple[float] = (0.01, 0.01, 1), render_objects:List=[]):
        
        self.pv_render.enable_joystick_actor_style()

        if isinstance(scene_source, pathlib.Path):
            background = pv.get_reader(scene_source).read()
            background = background.scale(scale_factor, inplace=False)
            
        elif isinstance(scene_source, np.ndarray):
            background = pv.UniformGrid(dimensions=(1920, 1080, 1), spacing=(0.01, 0.01, 1), origin=(0.0, 0.0, 0.0))
            background.point_data["values"] = scene_source.reshape((1920*1080, 3)) # order = 'C

        background = background.translate(-1 * np.array(background.center), inplace=False)
        
        if render_image:
           self.pv_render.add_mesh(background, rgb=True, opacity=1, name="image")
        else:
            self.pv_render.set_background('white')
            # generate white image
            self.pv_render.add_mesh(background, rgb=True, opacity=0, name="image")
            # generate grey image
            # self.pv_render.add_mesh(background, rgb=True, opacity=0.5, name="image")
            
            # Render the targeting objects
            for object in render_objects:
                mesh = self.pv_render.add_mesh(self.mesh_polydata[object], rgb=True, opacity=1)
                mesh.user_matrix = self.transformation_matrix
        
        self.pv_render.camera = self.camera.copy()
        self.pv_render.disable()
        self.pv_render.show()
        
        return self.pv_render.last_image
