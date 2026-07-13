# 動作手順
## パッケージの導入
```bash
$ cd happy_ws/src
$ ros2 pkg create time_topic --build-type ament_python --node-name time_pub_node
# ros2 pkg create <パッケージ名> --build-type ament_python --node-name <ノードファイル名> 
```
## ファイルの編集

## ビルド
```bash
$ colcon build
```
## 環境変数の設定
```bash
$ . ~/.bashrc
$ . install/setup.bash
$ . install/local_setup.bash
```
## 実行
```bash
$ ros2 run time_topic time_pub_node     # ros2 run <パッケージ名> <ノード名>
```