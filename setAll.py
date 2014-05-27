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
  ESC4PIN = "P9_42"

def armESCs(escList):
  for esc in escList:
    PWM.start(esc, 4, 50)
  
setGlobals()
escList = [ESC1PIN, ESC2PIN, ESC3PIN, ESC4PIN]
armESCs(escList)

# get command arguments
speed = float(sys.argv[1]) # from 4 - 10
dontTime = False
if (sys.argv[2] == "x"):
  dontTime = True
else:
  duration = float(sys.argv[2]) # number of seconds
  print "Setting all escs to speed " + sys.argv[1] \
  + " for duration " + sys.argv[2]

for esc in escList:
  PWM.set_duty_cycle(esc, speed)

if not dontTime:
  time.sleep(duration)
  for esc in escList:
    PWM.stop(esc)
  PWM.cleanup()
else:
  print "not timing this"
