#!/usr/bin/python
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import sys

import Adafruit_DHT

import pubnub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
 
pnconfig = PNConfiguration()
pnconfig.subscribe_key = "sub-c-a667485c-757f-11e8-9f59-fec9626a7085"
pnconfig.publish_key = "pub-c-cb2e18e3-a8b0-486a-bf82-2d9e9f670b7e"
pnconfig.ssl = False
 
pubnub = PubNub(pnconfig)


def publish_callback(result, status):
    pass
    # Handle PNPublishResult and PNStatus
 


# Parse command line parameters.

#if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
sensor = 2302
pin = 4
#else:
 #   print('usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#')
  #  print('example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO #4')
   # sys.exit(1)

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Un-comment the line below to convert the temperature to Fahrenheit.
# temperature = temperature * 9/5.0 + 32

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
#if humidity is not None and temperature is not None:
tweet = ('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
pubnub.publish().channel('twitter-input').message(tweet).async(publish_callback)
#else:
 #   print('Failed to get reading. Try again!')
  #  sys.exit(1)
