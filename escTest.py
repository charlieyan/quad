import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time
import sys

# FUNCTIONS
def setGlobals():
  global ESC1PIN
  global ESC2PIN 
  global ESC3PIN 
  global ESC4PIN 
  ESC1PIN = "P8_13"
  ESC2PIN = "P9_16"
  ESC3PIN = "P9_21"
  ESC4PIN = "P9_14"

def armESCs(escList):
  for esc in escList:
    PWM.start(esc, 4, 50)
  
setGlobals()
escList = [ESC1PIN, ESC2PIN, ESC3PIN, ESC4PIN]
armESCs(escList)

# get command arguments
escID = sys.argv[1] # from 0 - 3
esc = escList[int(escID)]
speed = float(sys.argv[2]) # from 4 - 10
duration = float(sys.argv[3]) # number of seconds
print "Setting esc on pin " + esc + " to speed " + sys.argv[2] \
  + " for duration " + sys.argv[3]

PWM.set_duty_cycle(esc, speed)

time.sleep(duration)

PWM.stop(esc)
PWM.cleanup()
