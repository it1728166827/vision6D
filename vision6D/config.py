import numpy as np
import pathlib
import os

CWD = pathlib.Path(os.path.abspath(__file__)).parent
GITROOT = CWD.parent
OP_DATA_DIR = GITROOT.parent / 'ossicles_6D_pose_estimation' / 'data'
YOLOV8_DATA_DIR = GITROOT.parent / 'yolov8'

#~ right ossicles
#* 455
IMAGE_PATH_455 = OP_DATA_DIR / "frames" /"CIP.455.8381493978235_video_trim" / "CIP.455.8381493978235_video_trim_0.png"
SEG_MASK_PATH_455 = YOLOV8_DATA_DIR / "runs" / "segment" / "CIP.455.8381493978235_video_trim_right_with_poses" / "seg_masks" / "ossicles" / "CIP.455.8381493978235_video_trim.png"
OSSICLES_MESH_PATH_455_right = OP_DATA_DIR / "surgical_planning" / "CIP.455.8381493978235_video_trim" / "mesh" / "processed_meshes" / "455_right_ossicles_processed.mesh"
FACIAL_NERVE_MESH_PATH_455_right = OP_DATA_DIR / "surgical_planning"/ "CIP.455.8381493978235_video_trim" / "mesh" / "processed_meshes" / "455_right_facial_nerve_processed.mesh"
CHORDA_MESH_PATH_455_right = OP_DATA_DIR / "surgical_planning"/ "CIP.455.8381493978235_video_trim" / "mesh" / "processed_meshes" / "455_right_chorda_processed.mesh"
SCALA_TYMPANI_MESH_PATH_455_right = OP_DATA_DIR / "surgical_planning"/ "CIP.455.8381493978235_video_trim" / "mesh" / "processed_meshes" / "455_right_scala_tympani_processed.mesh"

#* 5997
IMAGE_PATH_5997 = OP_DATA_DIR / "frames" /"CIP.5997.8381493978443_video_trim" / "CIP.5997.8381493978443_video_trim_0.png"
SEG_MASK_PATH_5997 = YOLOV8_DATA_DIR / "runs" / "segment" / "CIP.5997.8381493978443_video_trim_right_with_poses" / "seg_masks" / "ossicles" / "CIP.5997.8381493978443_video_trim.png"
OSSICLES_MESH_PATH_5997_right = OP_DATA_DIR / "surgical_planning" / "CIP.5997.8381493978443_video_trim" / "mesh" / "processed_meshes" / "5997_right_ossicles_processed.mesh"
FACIAL_NERVE_MESH_PATH_5997_right = OP_DATA_DIR / "surgical_planning"/ "CIP.5997.8381493978443_video_trim" / "mesh" / "processed_meshes" / "5997_right_facial_nerve_processed.mesh"
CHORDA_MESH_PATH_5997_right = OP_DATA_DIR / "surgical_planning"/ "CIP.5997.8381493978443_video_trim" / "mesh" / "processed_meshes" / "5997_right_chorda_processed.mesh"
SCALA_TYMPANI_MESH_PATH_5997_right = OP_DATA_DIR / "surgical_planning"/ "CIP.5997.8381493978443_video_trim" / "mesh" / "processed_meshes" / "5997_right_scala_tympani_processed.mesh"

#* 6088
IMAGE_PATH_6088 = OP_DATA_DIR / "frames" / "CIP.6088.1681356523312_video_trim" / "CIP.6088.1681356523312_video_trim_0.png"
SEG_MASK_PATH_6088 = YOLOV8_DATA_DIR / "runs" / "segment" / "CIP.6088.1681356523312_video_trim_right_with_poses" / "seg_masks" / "ossicles" / "CIP.6088.1681356523312_video_trim.png"
OSSICLES_MESH_PATH_6088_right = OP_DATA_DIR / "surgical_planning"/ "CIP.6088.1681356523312_video_trim" / "mesh" / "processed_meshes" / "6088_right_ossicles_processed.mesh"
FACIAL_NERVE_MESH_PATH_6088_right = OP_DATA_DIR / "surgical_planning"/ "CIP.6088.1681356523312_video_trim" / "mesh" / "processed_meshes" / "6088_right_facial_nerve_processed.mesh"
CHORDA_MESH_PATH_6088_right = OP_DATA_DIR / "surgical_planning"/ "CIP.6088.1681356523312_video_trim" / "mesh" / "processed_meshes" / "6088_right_chorda_processed.mesh"
SCALA_TYMPANI_MESH_PATH_6088_right = OP_DATA_DIR / "surgical_planning"/ "CIP.6088.1681356523312_video_trim" / "mesh" / "processed_meshes" / "6088_right_scala_tympani_processed.mesh"

#* 6108
IMAGE_PATH_6108 = OP_DATA_DIR / "frames" / "CIP.6108.1638408845868_video_trim" / "CIP.6108.1638408845868_video_trim_0.png"
SEG_MASK_PATH_6108 = YOLOV8_DATA_DIR / "runs" / "segment" / "CIP.6108.1638408845868_video_trim_right_with_poses" / "seg_masks" / "ossicles" / "CIP.6108.1638408845868_video_trim.png"
OSSICLES_MESH_PATH_6108_right = OP_DATA_DIR / "surgical_planning"/ "CIP.6108.1638408845868_video_trim" / "mesh" / "processed_meshes" / "6108_right_ossicles_processed.mesh"
FACIAL_NERVE_MESH_PATH_6108_right = OP_DATA_DIR / "surgical_planning"/ "CIP.6108.1638408845868_video_trim" / "mesh" / "processed_meshes" / "6108_right_facial_nerve_processed.mesh"
CHORDA_MESH_PATH_6108_right = OP_DATA_DIR / "surgical_planning"/ "CIP.6108.1638408845868_video_trim" / "mesh" / "processed_meshes" / "6108_right_chorda_processed.mesh"
SCALA_TYMPANI_MESH_PATH_6108_right = OP_DATA_DIR / "surgical_planning"/ "CIP.6108.1638408845868_video_trim" / "mesh" / "processed_meshes" / "6108_right_scala_tympani_processed.mesh"

#* 632
IMAGE_PATH_632 = OP_DATA_DIR / "frames" /"CIP.632.8381493978443_video_trim" / "CIP.632.8381493978443_video_trim_0.png"
SEG_MASK_PATH_632 = YOLOV8_DATA_DIR / "runs" / "segment" / "CIP.632.8381493978443_video_trim_right_with_poses" / "seg_masks" / "ossicles" / "CIP.632.8381493978443_video_trim.png"
OSSICLES_MESH_PATH_632_right = OP_DATA_DIR / "surgical_planning" / "CIP.632.8381493978443_video_trim" / "mesh" / "processed_meshes" / "632_right_ossicles_processed.mesh"
FACIAL_NERVE_MESH_PATH_632_right = OP_DATA_DIR / "surgical_planning"/ "CIP.632.8381493978443_video_trim" / "mesh" / "processed_meshes" / "632_right_facial_nerve_processed.mesh"
CHORDA_MESH_PATH_632_right = OP_DATA_DIR / "surgical_planning"/ "CIP.632.8381493978443_video_trim" / "mesh" / "processed_meshes" / "632_right_chorda_processed.mesh"
SCALA_TYMPANI_MESH_PATH_632_right = OP_DATA_DIR / "surgical_planning"/ "CIP.632.8381493978443_video_trim" / "mesh" / "processed_meshes" / "632_right_scala_tympani_processed.mesh"

#* 6320
IMAGE_PATH_6320 = OP_DATA_DIR / "frames" /"CIP.6320.5959167268122_video_trim" / "CIP.6320.5959167268122_video_trim_0.png"
SEG_MASK_PATH_6320 = YOLOV8_DATA_DIR / "runs" / "segment" / "CIP.6320.5959167268122_video_trim_right_with_poses" / "seg_masks" / "ossicles" / "CIP.6320.5959167268122_video_trim.png"
OSSICLES_MESH_PATH_6320_right = OP_DATA_DIR / "surgical_planning" / "CIP.6320.5959167268122_video_trim" / "mesh" / "processed_meshes" / "6320_right_ossicles_processed.mesh"
FACIAL_NERVE_MESH_PATH_6320_right = OP_DATA_DIR / "surgical_planning"/ "CIP.6320.5959167268122_video_trim" / "mesh" / "processed_meshes" / "6320_right_facial_nerve_processed.mesh"
CHORDA_MESH_PATH_6320_right = OP_DATA_DIR / "surgical_planning"/ "CIP.6320.5959167268122_video_trim" / "mesh" / "processed_meshes" / "6320_right_chorda_processed.mesh"
SCALA_TYMPANI_MESH_PATH_6320_right = OP_DATA_DIR / "surgical_planning"/ "CIP.6320.5959167268122_video_trim" / "mesh" / "processed_meshes" / "6320_right_scala_tympani_processed.mesh"

#* 6329
IMAGE_PATH_6329 = OP_DATA_DIR / "frames" /"CIP.6329.6010707468438_vieo_trim" / "CIP.6329.6010707468438_vieo_trim_0.png"
SEG_MASK_PATH_6329 = YOLOV8_DATA_DIR / "runs" / "segment" / "CIP.6329.6010707468438_vieo_trim_right_with_poses" / "seg_masks" / "ossicles" / "CIP.6329.6010707468438_vieo_trim.png"
OSSICLES_MESH_PATH_6329_right = OP_DATA_DIR / "surgical_planning" / "CIP.6329.6010707468438_vieo_trim" / "mesh" / "processed_meshes" / "6329_right_ossicles_processed.mesh"
FACIAL_NERVE_MESH_PATH_6329_right = OP_DATA_DIR / "surgical_planning"/ "CIP.6329.6010707468438_vieo_trim" / "mesh" / "processed_meshes" / "6329_right_facial_nerve_processed.mesh"
CHORDA_MESH_PATH_6329_right = OP_DATA_DIR / "surgical_planning"/ "CIP.6329.6010707468438_vieo_trim" / "mesh" / "processed_meshes" / "6329_right_chorda_processed.mesh"
SCALA_TYMPANI_MESH_PATH_6329_right = OP_DATA_DIR / "surgical_planning"/ "CIP.6329.6010707468438_vieo_trim" / "mesh" / "processed_meshes" / "6329_right_scala_tympani_processed.mesh"

#* 6602
IMAGE_PATH_6602 = OP_DATA_DIR / "frames" /"CIP.6602.7866163404219_video_trim" / "CIP.6602.7866163404219_video_trim_0.png"
SEG_MASK_PATH_6602 = YOLOV8_DATA_DIR / "runs" / "segment" / "CIP.6602.7866163404219_video_trim_right_with_poses" / "seg_masks" / "ossicles" / "CIP.6602.7866163404219_video_trim.png"
OSSICLES_MESH_PATH_6602_right = OP_DATA_DIR / "surgical_planning" / "CIP.6602.7866163404219_video_trim" / "mesh" / "processed_meshes" / "6602_right_ossicles_processed.mesh"
FACIAL_NERVE_MESH_PATH_6602_right = OP_DATA_DIR / "surgical_planning"/ "CIP.6602.7866163404219_video_trim" / "mesh" / "processed_meshes" / "6602_right_facial_nerve_processed.mesh"
CHORDA_MESH_PATH_6602_right = OP_DATA_DIR / "surgical_planning"/ "CIP.6602.7866163404219_video_trim" / "mesh" / "processed_meshes" / "6602_right_chorda_processed.mesh"
SCALA_TYMPANI_MESH_PATH_6602_right = OP_DATA_DIR / "surgical_planning"/ "CIP.6602.7866163404219_video_trim" / "mesh" / "processed_meshes" / "6602_right_scala_tympani_processed.mesh"

#* 6751
IMAGE_PATH_6751 = OP_DATA_DIR / "frames" /"CIP.6751.1844636424484_video_trim" / "CIP.6751.1844636424484_video_trim_0.png"
SEG_MASK_PATH_6751 = YOLOV8_DATA_DIR / "runs" / "segment" / "CIP.6751.1844636424484_video_trim_right_with_poses" / "seg_masks" / "ossicles" / "CIP.6751.1844636424484_video_trim.png"
OSSICLES_MESH_PATH_6751_right = OP_DATA_DIR / "surgical_planning" / "CIP.6751.1844636424484_video_trim" / "mesh" / "processed_meshes" / "6751_right_ossicles_processed.mesh"
FACIAL_NERVE_MESH_PATH_6751_right = OP_DATA_DIR / "surgical_planning"/ "CIP.6751.1844636424484_video_trim" / "mesh" / "processed_meshes" / "6751_right_facial_nerve_processed.mesh"
CHORDA_MESH_PATH_6751_right = OP_DATA_DIR / "surgical_planning"/ "CIP.6751.1844636424484_video_trim" / "mesh" / "processed_meshes" / "6751_right_chorda_processed.mesh"
SCALA_TYMPANI_MESH_PATH_6751_right = OP_DATA_DIR / "surgical_planning"/ "CIP.6751.1844636424484_video_trim" / "mesh" / "processed_meshes" / "6751_right_scala_tympani_processed.mesh"

#~ left ossicles
#* 6742
IMAGE_PATH_6742 = OP_DATA_DIR / "frames" / "CIP.6742.8381574350255_video_trim" / "CIP.6742.8381574350255_video_trim_0.png"
SEG_MASK_PATH_6742 = YOLOV8_DATA_DIR / "runs" / "segment" / "CIP.6742.8381574350255_video_trim_right_with_poses" / "seg_masks" / "ossicles" / "CIP.6742.8381574350255_video_trim.png"
OSSICLES_MESH_PATH_6742_left = OP_DATA_DIR / "surgical_planning"/ "CIP.6742.8381574350255_video_trim" / "mesh" / "processed_meshes" / "6742_left_ossicles_processed.mesh"
FACIAL_NERVE_MESH_PATH_6742_left = OP_DATA_DIR / "surgical_planning"/ "CIP.6742.8381574350255_video_trim" / "mesh" / "processed_meshes" / "6742_left_facial_nerve_processed.mesh"
CHORDA_MESH_PATH_6742_left = OP_DATA_DIR / "surgical_planning"/ "CIP.6742.8381574350255_video_trim" / "mesh" / "processed_meshes" / "6742_left_chorda_processed.mesh"
SCALA_TYMPANI_MESH_PATH_6742_left = OP_DATA_DIR / "surgical_planning"/ "CIP.6742.8381574350255_video_trim" / "mesh" / "processed_meshes" / "6742_left_scala_tympani_processed.mesh"

#* 6087
IMAGE_PATH_6087 = OP_DATA_DIR / "frames" /"CIP.6087.8415865242263_video_trim" / "CIP.6087.8415865242263_video_trim_0.png"
SEG_MASK_PATH_6087 = YOLOV8_DATA_DIR / "runs" / "segment" / "CIP.6087.8415865242263_video_trim_right_with_poses" / "seg_masks" / "ossicles" / "CIP.6087.8415865242263_video_trim.png"
OSSICLES_MESH_PATH_6087_left = OP_DATA_DIR / "surgical_planning" / "CIP.6087.8415865242263_video_trim" / "mesh" / "processed_meshes" / "6087_left_ossicles_processed.mesh"
FACIAL_NERVE_MESH_PATH_6087_left = OP_DATA_DIR / "surgical_planning"/ "CIP.6087.8415865242263_video_trim" / "mesh" / "processed_meshes" / "6087_left_facial_nerve_processed.mesh"
CHORDA_MESH_PATH_6087_left = OP_DATA_DIR / "surgical_planning"/ "CIP.6087.8415865242263_video_trim" / "mesh" / "processed_meshes" / "6087_left_chorda_processed.mesh"
SCALA_TYMPANI_MESH_PATH_6087_left = OP_DATA_DIR / "surgical_planning"/ "CIP.6087.8415865242263_video_trim" / "mesh" / "processed_meshes" / "6087_left_scala_tympani_processed.mesh"

# right ossicles
# actual pose for the 455 mesh
gt_pose_455_right = np.load(OP_DATA_DIR / "gt_poses" / "455_right_gt_pose.npy")
gt_pose_5997_right = np.load(OP_DATA_DIR / "gt_poses" / "5997_right_gt_pose.npy")
gt_pose_6088_right = np.load(OP_DATA_DIR / "gt_poses" / "6088_right_gt_pose.npy")
gt_pose_6108_right = np.load(OP_DATA_DIR / "gt_poses" / "6108_right_gt_pose.npy")
gt_pose_632_right = np.load(OP_DATA_DIR / "gt_poses" / "632_right_gt_pose.npy")

gt_pose_6320_right = np.load(OP_DATA_DIR / "gt_poses" / "6320_right_gt_pose.npy")
gt_pose_6329_right = np.load(OP_DATA_DIR / "gt_poses" / "6329_right_gt_pose.npy")
gt_pose_6602_right = np.load(OP_DATA_DIR / "gt_poses" / "6602_right_gt_pose.npy")
gt_pose_6751_right = np.load(OP_DATA_DIR / "gt_poses" / "6751_right_gt_pose.npy")

# left ossicles
gt_pose_6742_left = np.load(OP_DATA_DIR / "gt_poses" / "6742_left_gt_pose.npy")
gt_pose_6087_left = np.load(OP_DATA_DIR / "gt_poses" / "6087_left_gt_pose.npy")

