import rclpy                            # ros2のモジュール
from rclpy.node import Node             # ノードを使用可能にする

class HappyNode(Node):
    def __init__(self):
        print("ノードの生成")
        super().__init__("happy_node")              # ファイル名を指定
        self.get_logger().info("ハッピーワールド")    # ノードの処理

def main():
    print("プログラム開始")
    rclpy.init()
    node = HappyNode()
    node.destroy_node()
    rclpy.shutdown()
    print("プログラム終了")