# 作業手順

## ワークスペースの作成
```bash
$ mkdir -p ros2_ws/src
$ cd ros2_ws/src
```
## 初期パッケージの作成
```bash
$ ros2 pkg create mypkg --build-type ament_python
```
- package.xml, setup.pyに必要事項を記入
## パッケージのビルド
```bash
$ cd ros2_ws     # ワークスペースに移動
$ colcon build   # ビルド
$ source install/setup.bash        # パッケージの反映
$ source install/local_setup.bash  # パッケージの反映
$ source ~/.bashrc                 # パッケージの反映
$ ros2 pkg list | grep mypkg       # ros2がmypkgを認識してるか確認 --> mypkgと出ればok
```
## ノードの作成
- ros2_ws/src/mypkg/mypkg/talker.py
    - 数字をカウントしてトピック通信で送信
- ros2_ws/src/mypkg/mypkg/listener.py
    - talker.pyから値を受信
## パッケージの設定
- package.xmlに, ノードで使用したモジュールを追記
- setup.pyに, エントリポイントを追記 

## ビルド
```bash
$ cd ros2_ws                       # ワークスペースに移動
$ sudo rosdep update
$ sudo rosdep install -i --from-path src --rosdistro humble -y
# All required rosdeps installed successfully
$ colcon build
$ source ~/.bashrc
```
## talkerの実行 (端末１)
```bash
$ cd ros2_ws                       # ワークスペースに移動
$ ros2 run mypkg talker    
```
## listenerの実行 (端末２)
```bash
$ cd ros2_ws                       # ワークスペースに移動
$ source install/setup.bash        # パッケージの反映
$ source install/local_setup.bash  # パッケージの反映
$ source ~/.bashrc                 # パッケージの反映     
$ ros2 run mypkg listener
```