import Adafruit_BBIO.GPIO as AGPIO
import Adafruit_BBIO.PWM as PWM
from bbio import *
import time

#CONSTANTS
PULSETIME = 1100

def setupESC(pin):
  # set pin as OUTPUT
  AGPIO.setup(pin, AGPIO.OUT)
  # arm
  for armingTime in (0, 500):
    AGPIO.output(pin, AGPIO.HIGH)
    delayMicroseconds(PULSETIME)
    #time.sleep(1.1/1000) #1.1 milliseconds
    AGPIO.output(pin, AGPIO.LOW)
    delay(10-(PULSETIME/1000))
    #time.sleep(8.9/1000) #8.9 milliseconds
  print "Done arming " + pin

def drive(pin):
  # drive pin
  AGPIO.output(pin, AGPIO.HIGH)
  delayMicroseconds(PULSETIME) #high for 1.1 milliseconds
  AGPIO.output(pin, AGPIO.LOW)
  delay(10-(PULSETIME/1000)) #low for 8.9 milliseconds
  #total period is 10 milliseconds
  #frequency is 100 Hz

def setupGlobalPins():
  global ESC1PIN 
  ESC1PIN = "P9_11"
  global ESC2PIN 
  ESC2PIN = "P9_12"
  global ESC3PIN 
  ESC3PIN = "P9_13"
  global ESC4PIN 
  ESC4PIN = "P9_14"

def setup():
  setupGlobalPins()
  setupESC(ESC1PIN)
  # setupESC(ESC2PIN)
  # setupESC(ESC3PIN)
  # setupESC(ESC4PIN)

def loop():
  drive(ESC1PIN)

if __name__ == '__main__':
  setup()
  PWM.start("P9_14",11.5,100,0)
  time.sleep(5)
  PWM.stop(ESC1PIN)
  PWM.cleanup()