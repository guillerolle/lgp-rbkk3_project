from setuptools import find_packages, setup
from glob       import glob
import os

package_name = 'whkk3_simulation'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*launch.py')),
        (os.path.join('share', package_name, 'platform', 'launch'), glob('platform/launch/*launch.py')),
        (os.path.join('share', package_name, 'platform', 'config'), glob('platform/config/*yaml')),
        (os.path.join('share', package_name, 'sensors', 'launch'), glob('sensors/launch/*launch.py')),
        (os.path.join('share', package_name, 'sensors', 'config'), glob('sensors/config/*yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='duser',
    maintainer_email='duser@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
