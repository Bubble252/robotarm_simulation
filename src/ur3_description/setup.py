from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'ur3_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        # 安装 ROS 2 ament 索引文件
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        # 安装 package.xml
        ('share/' + package_name, ['package.xml']),
        # 安装 launch 文件夹里的 .launch.py 文件
        ('share/' + package_name + '/meshes', [
            'meshes/base_link.STL',
            'meshes/link1.STL',
            'meshes/link2.STL',
            'meshes/link3.STL',
            'meshes/link4.STL',
            'meshes/link5.STL',
            'meshes/link6.STL',
        ]),        
        
        
        
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        # 安装 URDF 文件（假设在 urdf 文件夹下）
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.urdf')),
        # 安装 mesh 文件（假设在 meshes 文件夹下）
        (os.path.join('share', package_name, 'meshes'), glob('meshes/*.STL')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntu',
    maintainer_email='ubuntu@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # 如有节点可以在这里注册，例如：
            # 'node_name = ur3_description.node_file:main',
        ],
    },
    include_package_data=True,
)

