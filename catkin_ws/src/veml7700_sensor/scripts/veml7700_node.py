#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
from adafruit_veml7700 import VEML7700
import board
import busio

def veml7700_publisher():
    # Initialize ROS node
    rospy.init_node('veml7700_node', anonymous=True)

    # Create a publisher
    pub = rospy.Publisher('lux', Float32, queue_size=10)

    # Set the rate at which the loop runs
    rate = rospy.Rate(1)  # 1 Hz

    # Initialize the sensor
    i2c = busio.I2C(board.SCL, board.SDA)
    veml7700 = VEML7700(i2c)

    while not rospy.is_shutdown():
        # Read the lux value from the sensor
        lux_value = veml7700.lux

        # Log the lux value
        rospy.loginfo(f"Lux: {lux_value}")

        # Publish the lux value
        pub.publish(lux_value)

        # Sleep to maintain loop rate
        rate.sleep()

if __name__ == '__main__':
    try:
        veml7700_publisher()
    except rospy.ROSInterruptException:
        pass
