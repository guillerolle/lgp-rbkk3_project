from setuptools import find_packages, setup
from glob       import glob
import os

package_name = 'ridgeback_description'
# urdf_glob = 
# urdf_files = [i for i in (f for f in glob('urdf/*', recursive=False) if os.path.isfile(f))]
# print(urdf_files)

def list_files(pattern):
    globs = glob(pattern, recursive=False)
    return [i for i in (f for f in globs if os.path.isfile(f))]

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    #urdf_glob = glob('urdf/**', recursive=True)
    #urdf_files = [i for i in (f for f in urdf_glob if os.path.isfile(f))]
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*launch.py')),
        (os.path.join('share', package_name, 'urdf'), list_files('urdf/*')),
        (os.path.join('share', package_name, 'urdf', 'configs'), list_files('urdf/configs/*')),
        (os.path.join('share', package_name, 'urdf', 'accessories'), list_files('urdf/accessories/*')),
        (os.path.join('share', package_name, 'meshes'), list_files('meshes/*')),
        (os.path.join('share', package_name, 'rviz'), list_files('rviz/*.rviz')),
        #(os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
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
