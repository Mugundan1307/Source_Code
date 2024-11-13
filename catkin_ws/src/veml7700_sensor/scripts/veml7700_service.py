#!/usr/bin/env python3

import rospy
from veml7700_sensor.srv import GetLux, GetLuxResponse
from adafruit_veml7700 import VEML7700
import board
import busio

def handle_get_lux(req):
    # Initialize the sensor
    i2c = busio.I2C(board.SCL, board.SDA)
    veml7700 = VEML7700(i2c)

    # Read the lux value from the sensor
    lux_value = veml7700.lux

    # Return the lux value in the service response
    return GetLuxResponse(lux_value)

def veml7700_service_server():
    rospy.init_node('veml7700_service_server')
    service = rospy.Service('get_lux', GetLux, handle_get_lux)
    rospy.loginfo("VEML7700 Lux service ready")
    rospy.spin()

if __name__ == "__main__":
    veml7700_service_server()
