#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import cv2
import numpy as np

class SterownikRobota(Node):
    def __init__(self):
        super().__init__('sterownik_node')
        
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        
        self.timer = self.create_timer(0.1, self.timer_callback)
        
        self.window_name = "Interfejs sterowania"
        self.width, self.height = 512, 512
        
        self.canvas = np.zeros((self.height, self.width, 3), np.uint8)
        
        cv2.line(self.canvas, (0, self.height//2), (self.width, self.height//2), (0, 0, 255), 2)
        cv2.putText(self.canvas, "PRZÓD", (self.width//2-50, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
        cv2.putText(self.canvas, "TYŁ", (self.width//2-30, 380), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    def timer_callback(self):
        cv2.imshow(self.window_name, self.canvas)
        cv2.setMouseCallback(self.window_name, self.obsluga_myszki)
        cv2.waitKey(1)

    def obsluga_myszki(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            msg = Twist()
        
            if y < self.height / 2:
                msg.linear.x = 0.2  
                self.get_logger().info('Kliknięto GÓRA: Robot jedzie do przodu')
            else:
                msg.linear.x = -0.2 
                self.get_logger().info('Kliknięto DÓŁ: Robot jedzie do tyłu')
            
            self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = SterownikRobota()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()