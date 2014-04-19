import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import ctypes, time
libc = ctypes.CDLL('libc.so.6')

#CONSTANTS
PULSETIME = 1100

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

def setupGlobalPins():
  global ESC1PIN 
  ESC1PIN = "P9_11"
  global ESC2PIN 
  ESC2PIN = "P9_12"
  global ESC3PIN 
  ESC3PIN = "P9_13"
  global ESC4PIN 
  ESC4PIN = "P9_14"

def main():
  setupGlobalPins()
  setupESC(ESC1PIN)