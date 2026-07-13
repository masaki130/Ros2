# setup.pyのエントリポイントにhappy_node2を追記
import rclpy                            # ros2のモジュール
from rclpy.node import Node             # ノードを使用可能にする

class HappyNode2(Node):
    def __init__(self):
        print("ノードの生成")
        super().__init__("happy_node2")                                 # ファイル名を指定
        self.timer = self.create_timer(1.0, self.timer_callback)       # タイマの生成, 1[s]毎にtimer_callback関数を実行

    def timer_callback(self):
        self.get_logger().info("ハッピーワールド２")

def main():
    print("プログラム開始")
    rclpy.init()
    node = HappyNode2()
    rclpy.spin(node)        # コールバックを何度も呼び出す
    node.destroy_node()
    rclpy.shutdown()
    print("プログラム終了")