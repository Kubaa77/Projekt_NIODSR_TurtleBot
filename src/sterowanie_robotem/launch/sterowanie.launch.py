import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    
    gazebo_launch_dir = os.path.join(get_package_share_directory('turtlebot3_gazebo'), 'launch')
    
    return LaunchDescription([
        
        SetEnvironmentVariable(name='TURTLEBOT3_MODEL', value='burger'),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(gazebo_launch_dir, 'empty_world.launch.py')
            )
        ),

        Node(
            package='sterowanie_robotem',
            executable='sterownik_node',
            name='moj_sterownik',
            output='screen'
        ),
    ])