#!/usr/bin/env python3

from your_package.srv import GetLux, GetLuxResponse
import rospy
from vl6180 import VL6180  # Make sure you have a library to interface with the VL6180 sensor

def handle_get_lux(req):
    sensor = VL6180()
    lux = sensor.read_lux()
    return GetLuxResponse(lux)

def lux_service_server():
    rospy.init_node('lux_service_server')
    s = rospy.Service('get_lux', GetLux, handle_get_lux)
    rospy.loginfo("Ready to provide lux readings.")
    rospy.spin()

if __name__ == "__main__":
    lux_service_server()
