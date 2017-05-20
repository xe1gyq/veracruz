#!/usr/bin/python

import atexit
import dweepy
import signal
import sys
import time

from upm import pyupm_grove as grove

light = grove.GroveLight(0)
button = grove.GroveButton(8)

dweetiodatasource = {}
dweetiothingname = "ilab_xpuhil"

def SIGINTHandler(signum, frame):
	raise SystemExit

def exitHandler():
	print "Exiting"
        time.sleep(2)
        dweetiodatasource['alive'] = "0"
        dweetiodatasource['luxes'] =  0
        dweetiodatasource['message'] = "None"
        dweepy.dweet_for(dweetiothingname, dweetiodatasource)
	sys.exit(0)

atexit.register(exitHandler)
signal.signal(signal.SIGINT, SIGINTHandler)

if __name__ == '__main__':

    message = "Hello Xpuhil!"

    while True:

        luxes = light.value()
        buttonvalue = button.value()

        print(button.name(), ' value is ', button.value())
        dweetiodatasource['alive'] = buttonvalue
        dweetiodatasource['luxes'] =  luxes
        dweetiodatasource['message'] = message
        dweepy.dweet_for(dweetiothingname, dweetiodatasource)

        time.sleep(1)
