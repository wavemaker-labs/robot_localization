from launch import LaunchDescription
import launch_ros.actions
import os
import yaml
from launch.substitutions import EnvironmentVariable
import pathlib
import launch.actions
from launch.actions import DeclareLaunchArgument


def generate_launch_description():
    parameters_file_dir = pathlib.Path(__file__).resolve().parent
    parameters_file_path = parameters_file_dir /'test_ukf_localization_node_bag3.yaml'    
    os.environ['FILE_PATH'] = str(parameters_file_dir)
    return LaunchDescription([
       launch.actions.DeclareLaunchArgument(
            'output_final_position',
            default_value='false'),
        launch.actions.DeclareLaunchArgument(
            'output_location',
	    default_value='ukf3.txt'),
		
	#*****test_ukf_localization_node_bag3.test***** 
	launch_ros.actions.Node(
            package='robot_localization', node_executable='se_node', node_name='test_ukf_localization_node_bag3_ukf',
	    output='screen',
	    parameters=[
                parameters_file_path,
                str(parameters_file_path),
                [EnvironmentVariable(name='FILE_PATH'), os.sep, 'test_ukf_localization_node_bag3.yaml'],
           ],
           ),
        launch_ros.actions.Node(
            package='robot_localization', node_executable='test_ukf_localization_node_bag3', node_name='test_ukf_localization_node_bag3_pose',
            output='screen',
	parameters=[
                parameters_file_path,
                str(parameters_file_path),
                [EnvironmentVariable(name='FILE_PATH'), os.sep, 'test_ukf_localization_node_bag3.yaml'],
        ],
	),
])













