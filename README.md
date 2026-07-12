# ROS2 installer

## how to use

```bash
$ git clone https://github.com/ryuichiueda/ros2_setup_scripts
$ cd ros2_setup_scripts
$ ./setup.bash
### don't add sudo to the head ###
$ source ~/.bashrc
$ ros2
### usage appears if ok ###
```
## 動作確認
- 別々のターミナルで以下を実行すると、ノード間通信を確認できる
```bash
$ ros2 run demo_nodes_py talker     # 端末１
$ ros2 run demo_nodes_py listener   # 端末２
```
## verified in

* Ubuntu 20.04 LTS on WSL2
* Ubuntu 22.04 LTS on WSL2
* Ubuntu 22.04 LTS
* Ubuntu 24.04 LTS
