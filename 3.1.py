import rospy
from geometry_msgs.msg import Twist

LIN_VEL = 0.5  
ANG_VEL = 1.0  
SIDE_LENGTH = 1.0 

def draw_square():
  """
  Function to make the turtle draw a square.
  """
  pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
  move_msg = Twist()

  # Move forward for one side
  move_msg.linear.x = LIN_VEL
  rospy.loginfo("Moving forward...")
  duration = SIDE_LENGTH / LIN_VEL
  pub.publish(move_msg)
  rospy.sleep(duration)

  # Rotate 90 degrees for the next side
  move_msg.linear.x = 0.0
  move_msg.angular.z = ANG_VEL
  rospy.loginfo("Turning...")
  duration = (3.14 / 2) / ANG_VEL
  pub.publish(move_msg)
  rospy.sleep(duration)

  for _ in range(3):
    draw_square()

def main():
  rospy.init_node('square_drawer')

  # Wait for ROS services
  rospy.wait_for_service('/turtle1/cmd_vel')

  # Draw squares in an infinite loop
  while not rospy.is_shutdown():
    draw_square()

if __name__ == '__main__':
  main()