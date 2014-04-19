import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
from bbio import *
import time

#CONSTANTS
ESC1PIN "P9_11"
ESC2PIN "P9_12"
ESC3PIN "P9_13"
ESC4PIN "P9_14"
PULSETIME 1100

def setupESC(pin):
  # set pin as OUTPUT
  GPIO.setup(pin, GPIO.OUT)
  # arm
  for armingTime in (0, 500):
    GPIO.output(pin, GPIO.HIGH)
    delayMicroseconds(PULSETIME)
    #time.sleep(1.1/1000) #1.1 milliseconds
    GPIO.output(pin, GPIO.LOW)
    delay(10-(PULSETIME/1000))
    #time.sleep(8.9/1000) #8.9 milliseconds
  print "Done arming " + pin
  return

def test():
  GPIO.setup("P9_12",GPIO.OUT)
  for i in range(0,20):
    GPIO.output("P9_12",GPIO.HIGH)
    time.sleep(1)
    GPIO.output("P9_12",GPIO.LOW)
    time.sleep(1)
  GPIO.cleanup()

def loop():
  pulseTime = 1200
  GPIO.output(ESC1PIN,GPIO.HIGH)
  delayMicroseconds(pulseTime)
  GPIO.output(ESC1PIN,GPIO.LOW)
  delay(10-(pulseTime/1000))
  
def setup():
  setupESC(ESC1PIN)

def main():
  setupESC(ESC1PIN)
  time.sleep(4)
  print "Starting drive"
  GPIO.cleanup()

if __name__ == '__main__':
  run(setup,loop)  
