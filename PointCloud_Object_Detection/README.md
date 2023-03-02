# Center-based 3D Object Detection and Tracking on live PointCloud data 
 This project was developed by Kshitiz Kumar, a Core Member of Epoch Club(2022-2023).
	
## Features
- Anchor-free method
- Support multiple point cloud datasets with different patterns.

## Setup
1. Install dependencies (Following dependencies have been tested.).
	- CUDA Toolkit: 10.2
	- python: 3.8
	- numpy: 1.23.1
	- pytorch: 1.8.2
	- ros: melodic
	- rospkg: 1.4.0
	- ros_numpy: 0.0.3 (sudo apt-get install ros-$ros_release-ros-numpy)
	- pyyaml
	- argparse 
2. Build this project
```bash
python3 setup.py develop
```

## Usage
1. Run ROS.
```
roscore
```
2. Move to 'tools' directory and run test_ros.py (pretrained model: ../pt/object_model_1.pt or ../pt/object_model_2.pt).
```
cd tools
python3 test_ros.py --pt ../pt/object_model_1.pt
```
3. Play rosbag. (Please adjust the ground plane to 0m and keep it horizontal. The topic of pointcloud2 should be /object/lidar)
```
rosbag play [bag path]
```
4. Visualize the results.
```
rviz -d rviz.rviz
```

## Acknowledgements
- This project was inspired by the anchor-free method, CenterPoint, which was proposed in this [paper](https://arxiv.org/abs/2006.11275).


