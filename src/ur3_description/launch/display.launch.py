from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():
    # 获取 URDF 文件路径
    urdf_file_path = os.path.join(
        os.getenv('HOME'),
        '桌面', 'arm', 'ros2_ws2', 'src',
        'ur3_description', 'urdf', 'ur3.urdf'
    )

    # 读取 URDF 内容作为 robot_description 参数
    with open(urdf_file_path, 'r') as infp:
        robot_description = infp.read()

    return LaunchDescription([
        # 发布 URDF → TF
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_description}]
        ),

        # 可视化可调关节状态
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            output='screen'
        ),

        # 启动 RViz2
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen'
        )
    ])

