import logging
import pathlib
import os

import pytest
import pyvista as pv
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2
from scipy.spatial.transform import Rotation as R
from pytest_lazyfixture  import lazy_fixture

import vision6D as vis

logger = logging.getLogger("vision6D")

np.set_printoptions(suppress=True)

CWD = pathlib.Path(os.path.abspath(__file__)).parent
DATA_DIR = CWD / 'data'
IMAGE_PATH = DATA_DIR / "RL_20210304_0.jpg"
BACKGROUND_PATH = DATA_DIR / "black_background.jpg"

OSSICLES_PATH = DATA_DIR / "ossicles_001_colored_not_centered.ply"
FACIAL_NERVE_PATH = DATA_DIR / "facial_nerve_001_colored_not_centered.ply"
CHORDA_PATH = DATA_DIR / "chorda_001_colored_not_centered.ply"

OSSICLES_PATH_NO_COLOR = DATA_DIR / "ossicles_001_not_colored.ply"
FACIAL_NERVE_PATH_NO_COLOR = DATA_DIR / "facial_nerve_001_not_colored.ply"
CHORDA_PATH_NO_COLOR = DATA_DIR / "chorda_001_not_colored.ply"

OSSICLES_MESH_PATH = DATA_DIR / "5997_right_output_mesh_from_df.mesh"
FACIAL_NERVE_MESH_PATH = DATA_DIR / "5997_right_facial_nerve.mesh"
CHORDA_MESH_PATH = DATA_DIR / "5997_right_chorda.mesh"

OSSICLES_TRANSFORMATION_MATRIX = np.array(
            [[-0.84071277,  0.04772072, -0.53937443,  4.14284471],
            [-0.08303411, -0.99568925,  0.0413309,  30.05524976],
            [-0.53507698,  0.0795339,   0.84105112, 15.71920575],
            [ 0.,          0.,          0. ,         1.,        ]])

@pytest.fixture
def app():
    return vis.App(True)
    # return vis.App(False)
    
@pytest.fixture
def configured_app(app):
    app.load_image(IMAGE_PATH, [0.01, 0.01, 1])
    app.set_transformation_matrix(OSSICLES_TRANSFORMATION_MATRIX)
    app.load_meshes({'ossicles': OSSICLES_PATH_NO_COLOR, 'facial_nerve': FACIAL_NERVE_PATH_NO_COLOR, 'chorda': CHORDA_PATH_NO_COLOR})
    app.bind_meshes("ossicles", "g", ['facial_nerve', 'chorda'])
    app.bind_meshes("chorda", "h", ['ossicles', 'facial_nerve'])
    app.bind_meshes("facial_nerve", "j", ['ossicles', 'chorda'])
    app.set_reference("ossicles")
    return app

def test_create_app(app):
    assert isinstance(app, vis.App)

def test_load_image(app):
    app.load_image(IMAGE_PATH, scale_factor=[0.01, 0.01, 1])
    app.set_reference("image")
    app.plot()

def test_load_mesh_from_ply(configured_app):
    configured_app.plot()
    
def test_load_mesh_from_polydata(app):
    app.set_transformation_matrix(np.eye(4))
    app.load_meshes({'sephere': pv.Sphere(radius=1)})
    app.bind_meshes("sephere", "g", ['sephere'])
    app.plot()

def test_load_mesh_from_meshfile(app):
    app.load_image(IMAGE_PATH, [0.01, 0.01, 1])
    app.set_reference("ossicles")
    app.set_transformation_matrix(OSSICLES_TRANSFORMATION_MATRIX)
    app.load_meshes({'ossicles': OSSICLES_MESH_PATH, 'facial_nerve': FACIAL_NERVE_MESH_PATH, 'chorda': CHORDA_MESH_PATH})
    app.bind_meshes("ossicles", "g", ['facial_nerve', 'chorda'])
    app.bind_meshes("chorda", "h", ['ossicles', 'facial_nerve'])
    app.bind_meshes("facial_nerve", "j", ['ossicles', 'chorda'])
    app.plot()
    
def test_plot_render(configured_app):
    configured_app.plot()
    image_np = configured_app.render_scene(BACKGROUND_PATH, [0.01, 0.01, 1], False)
    image = Image.fromarray(image_np)
    image.save(DATA_DIR / "res_render_whole_plot_render_function.png")
    
def test_render_image(app):
    image_np = app.render_scene(IMAGE_PATH, [0.01, 0.01, 1], True)
    image = Image.fromarray(image_np)
    image.save(DATA_DIR / "image1.png")
    
def test_render_ossicles(app):
    app.set_transformation_matrix(OSSICLES_TRANSFORMATION_MATRIX)
    app.load_meshes({'ossicles': OSSICLES_MESH_PATH, 'facial_nerve': FACIAL_NERVE_MESH_PATH, 'chorda': CHORDA_MESH_PATH})
    image_np = app.render_scene(BACKGROUND_PATH, [0.01, 0.01, 1], False, 'ossicles')
    image = Image.fromarray(image_np)
    image.save(DATA_DIR / "res_render1.png")
    
def test_render_whole(app):
    app.set_transformation_matrix(OSSICLES_TRANSFORMATION_MATRIX)
    app.load_meshes({'ossicles': OSSICLES_MESH_PATH, 'facial_nerve': FACIAL_NERVE_MESH_PATH, 'chorda': CHORDA_MESH_PATH})
    image_np = app.render_scene(BACKGROUND_PATH, [0.01, 0.01, 1], False)
    image = Image.fromarray(image_np)
    image.save(DATA_DIR / "res_render_whole.png")

# @pytest.mark.parametrize(
#     "_app, expected_RT", 
#     (
#         (lazy_fixture("app"), np.eye(4)),
#     )
# )
def test_pnp_with_cube(app):
    # Reference:
    # https://learnopencv.com/head-pose-estimation-using-opencv-and-dlib/
    # https://www.cse.psu.edu/~rtc12/CSE486/lecture12.pdf: Lecture 12: Camera Projection PPT
    
    # Set camera intrinsics
    app.set_camera_intrinsics(focal_length=2015, width=1920, height=1080)
    
    # Set camera extrinsics
    app.set_camera_extrinsics(position=(0, 0, 0), focal_point=(0, 0, 1), viewup=(0,-1,0))
    
    # Load a cube mesh
    cube = pv.Cube(center=(0,0,0))

    # # Create a RT transformation matrix manually
    # t = np.array([0,0,5])
    # r = R.from_rotvec((0,0.7,0)).as_matrix()
    # RT = np.vstack((np.hstack((r, t.reshape((-1,1)))), [0,0,0,1]))
    
    RT = np.array([[0.64706274, -0.59506601, -0.47666158,  0],
                [0.01325321,  0.63386593, -0.77332939,  0],
                [0.76232156,  0.49407533,  0.41803756,  5],
                [0.,          0.,          0.,          1]])
    
    app.set_transformation_matrix(RT)
    
    app.load_meshes({'cube': cube}) # Pass parameter of desired RT applied to
    
    app.plot()
    
    # Create rendering
    render = app.render_scene(BACKGROUND_PATH, (0.01, 0.01, 1), False)
    mask_render = vis.utils.color2binary_mask(vis.utils.change_mask_bg(render, [255, 255, 255], [0, 0, 0]))
    plt.imshow(render); plt.show()  
    
    # Create 2D-3D correspondences
    pts2d, pts3d = vis.utils.create_2d_3d_pairs(mask_render, render, scale=[1,1,1])
    
    logger.debug(f"The total points are {pts3d.shape[0]}")

    pts2d = pts2d.astype('float32')
    pts3d = pts3d.astype('float32')
    camera_intrinsics = app.camera_intrinsics.astype('float32')
    
    predicted_pose = vis.utils.solvePnP(camera_intrinsics, pts2d, pts3d)
    # predicted_pose = predicted_pose[:3]
    
    assert np.isclose(predicted_pose, RT, atol=1e-2).all()