import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/masaki/ros2_setup_scripts/ros2_ws/install/mypkg'
