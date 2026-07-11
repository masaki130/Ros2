# ROS2 installer

## how to use

```bash
$ ./setup.bash
### don't add sudo to the head ###
$ source ~/.bashrc
$ ros2
### usage appears if ok ###
```
## 動作確認
- 端末１で以下を実行
```
$ ros2 run demo_nodes_py talker
```
- 端末２で以下を実行
```
$ ros2 run demo_nodes_py listener
```
## verified in

* Ubuntu 20.04 LTS on WSL2
* Ubuntu 22.04 LTS on WSL2
* Ubuntu 22.04 LTS
* Ubuntu 24.04 LTS
