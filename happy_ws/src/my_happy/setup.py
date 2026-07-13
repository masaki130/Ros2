from setuptools import find_packages, setup

package_name = 'my_happy'

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
    maintainer_email='pasapasamasaki0@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'happy_node = my_happy.happy_node:main',
            "happy_node2 = my_happy.happy_node2:main",
            "happy_node3 = my_happy.happy_node3:main",
            "happy_pub_node = my_happy.happy_pub_node:main"
        ],
    },
)
