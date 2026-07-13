# Gazeboでturtlebot3を動かす

## アップデート
```bash
$ sudo apt update
$ sudo apt upgrade
```
## Gazeboのインストール
```bash
$ sudo apt install ros-humble-gazebo-*
```
## 関連パッケージのインストール
```bash
$ sudo apt install ros-humble-cartographer
$ sudo apt install ros-humble-cartographer-ros
$ sudo apt install ros-humble-dynamixel-sdk
$ sudo apt install ros-humble-turtlebot3-msgs
$ sudo apt install ros-humble-turtlebot3

```
## ワークスペースの作成
```bash
$ mkdir -p turtlebot3_ws/src
```
## Turtlebot3をクローン
```bash
$ cd turtlebot3_ws/src
$ git clone --depth 1 -b humble https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
```
## ビルド
```bash
$ cd ../ && colcon build --symlink-install                  # ワークスペースへ移動
$ sourse install/setup.bash                                 # 環境変数の設定
$ sourse install/local_setup.bash
```
## シュミレーションを起動
```bash
$ export TURTLEBOT3_MODEL=waffle                            # Turtlebot3のモデルを指定
$ ros2 launch turtlebot3_gazebo empty_world.launch.py       # 空のワールドを起動
# ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py  # デフォルトのTurtlebot3の環境
```
## 環境
- Ubuntu 22.04 on wsl2
- python 3.10