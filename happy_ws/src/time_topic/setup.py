from setuptools import find_packages, setup

package_name = 'time_topic'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='masaki',
    maintainer_email='masaki@example.com',
    description='TODO: Package description',
    license='BSD-3-clause',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'time_pub_node = time_topic.time_pub_node:main'
        ],
    },
)
