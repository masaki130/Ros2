# 動作手順
## パッケージの導入
```bash
$ cd happy_ws/src
$ ros2 pkg create time_topic --build-type ament_python --node-name time_pub_node
# ros2 pkg create <パッケージ名> --build-type ament_python --node-name <ノードファイル名> 
```
## ファイルの編集
- nodeファイル
- package.xml
- setup.py

## ビルド
```bash
$ conda deactivate                       # python 3.10にするため
$ cd happy_ws                            # ワークスペースに移動
$ colcon build
```
## 環境変数の設定
```bash
$ . install/setup.bash
$ . install/local_setup.bash
$ ros2 pkg list | grep happy_topic       # パッケージを認識できてるか確認
```
## 実行
```bash
$ ros2 run time_topic time_pub_node     # ros2 run <パッケージ名> <ノード名>
```