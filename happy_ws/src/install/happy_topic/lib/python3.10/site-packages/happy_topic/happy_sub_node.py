# setup.pyのエントリポイントにhappy_pub_nodeを追記
import rclpy                            # ros2のモジュール
from rclpy.node import Node             # ノードを使用可能にする
from std_msgs.msg import String         # 文字列用

class HappySub(Node):
    def __init__(self):                 # コンストラクタ
        print("ノードの生成")
        super().__init__("happy_sub_node")                             # ファイル名を指定
        self.sub = self.create_subscription(String, "topic", self.timer_callback, 10)          # パブリッシャの生成

    def timer_callback(self, msg):           # コールバック
        self.get_logger().info(f"サブスクライブ：{msg.data}")

def main():
    print("プログラム開始")
    rclpy.init()
    node = HappySub()
    rclpy.spin(node)        # コールバックを何度も呼び出す
    node.destroy_node()
    rclpy.shutdown()
    print("プログラム終了")