#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32
import board
import busio
import adafruit_vl6180x

def read_lux(sensor):
    return sensor.read_lux(adafruit_vl6180x.ALS_GAIN_1)

def range_mm(sensor):

    return sensor.range

def publish_lux():
    # Initialize the ROS node
    rospy.init_node('vl6180_node', anonymous=True)

    # Create a publisher to the 'lux' topic
    pub = rospy.Publisher('/vl6180lux', Float32, queue_size=10)

def publish_range():
    # Initialize the ROS node
    rospy.init_node('vl6180_node', anonymous=True)

    # Create a publisher to the 'lux' topic
    pub = rospy.Publisher('/vl6180range', Float32, queue_size=10)

    # Initialize the I2C bus and sensor
    i2c = busio.I2C(board.SCL, board.SDA)
    sensor = adafruit_vl6180x.VL6180X(i2c)

    # Set the rate of publishing (1 Hz)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        # Read the lux value from the sensor
        lux_value = read_lux(sensor)
        range_value = range_mm(sensor)
        # Log the lux value
        rospy.loginfo("Lux value: %f", lux_value)
        rospy.loginfo("Range : %f", range_value)
        # Publish the lux value
        pub.publish(lux_value)
        pub.publish(range_value)

        # Sleep for the specified rate
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_lux()
        publish_range()
    except rospy.ROSInterruptException:
        pass
