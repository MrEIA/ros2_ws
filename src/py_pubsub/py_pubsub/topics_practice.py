import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist


class PrácticePublisher(Node):

   def __init__(self):
      super().__init__('topics_practice')
      self.publish_vel = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
      timer_period = 0.5  # seconds
      self.timer_ = self.create_timer(timer_period, self.timer_callback)
      self.count_ = 0

   def timer_callback(self):
      msg = String()
      msg.data = 'Aplication try to starts: %d' % self.count_
      self.publish_vel.publish(msg)
      self.get_logger().info('Publishing by new node: "%s"' % msg.data)
      self.count_ += 1


def main(args=None):
   rclpy.init(args=args)

   publisher = PrácticePublisher()

   rclpy.spin(publisher)

   publisher.destroy_node()
   rclpy.shutdown()


if __name__ == '__main__':
   main()