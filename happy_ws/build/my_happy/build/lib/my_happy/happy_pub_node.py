# setup.pyのエントリポイントにhappy_pub_nodeを追記
import rclpy                            # ros2のモジュール
from rclpy.node import Node             # ノードを使用可能にする
from std_msgs.msg import String         # 文字列用

class HappyPub(Node):
    def __init__(self):                 # コンストラクタ
        print("ノードの生成")
        super().__init__("happy_pub_node")                             # ファイル名を指定
        self.pub = self.create_publisher(String, "topic", 10)          # パブリッシャの生成
        self.timer = self.create_timer(1.0, self.timer_callback)       # タイマの生成, 1[s]毎にtimer_callback関数を実行
        self.i = 10

    def timer_callback(self):           # コールバック
        msg = String()                  # 型を明記
        if self.i > 0:
            msg.data = f"ハッピーカウントダウン {self.i}"
        elif self.i == 0:
            msg.data = f"発射！"
        else:
            msg.data = f"経過時間：{-self.i}"
        self.pub.publish(msg)
        self.get_logger().info(f"パブリッシュ：{msg.data}")
        self.i -= 1

def main():
    print("プログラム開始")
    rclpy.init()
    node = HappyPub()
    rclpy.spin(node)        # コールバックを何度も呼び出す
    node.destroy_node()
    rclpy.shutdown()
    print("プログラム終了")