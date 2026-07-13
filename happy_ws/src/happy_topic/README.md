# トピック通信
## Publisher
```bash
# 端末１で以下を実行
$ cd ~/ros2_setup_scripts/happy_ws
$ conda deactivate
$ colcon build
$ . install/setup.bash
$ . install/local_setup.bash
$ ros2 pkg list | grep happy_topic
$ ros2 run happy_topic happy_pub_node
```

## Subscriber
```bash
# 端末２で以下を実行
$ cd ~/ros2_setup_scripts/happy_ws
$ conda deactivate
$ colcon build
$ . install/setup.bash
$ . install/local_setup.bash
$ ros2 pkg list | grep happy_topic
$ ros2 run happy_topic happy_sub_node
```