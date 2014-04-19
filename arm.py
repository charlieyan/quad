import Adafruit_BBIO.GPIO as GPIO2
import Adafruit_BBIO.PWM as PWM2
from bbio import *
import ctypes, time
libc = ctypes.CDLL('libc.so.6')

#CONSTANTS
PULSETIME = 1100

def delay(ms):
  ms = int(ms*1000)
  libc.usleep(ms)

def delayMicroseconds(us):
  libc.usleep(int(us))

def setupESC(pin):
  # set pin as OUTPUT
  GPIO2.setup(pin, GPIO2.OUT)
  # arm
  for armingTime in (0, 500):
    GPIO2.output(pin, GPIO2.HIGH)
    delayMicroseconds(PULSETIME)
    #time.sleep(1.1/1000) #1.1 milliseconds
    GPIO2.output(pin, GPIO2.LOW)
    delay(10-(PULSETIME/1000))
    #time.sleep(8.9/1000) #8.9 milliseconds
  print "Done arming " + pin
  return

def drive(pin):
  # drive pin
  GPIO2.output(pin, GPIO2.HIGH)
  delayMicroseconds(PULSETIME) #high for 1.1 milliseconds
  GPIO2.output(pin, GPIO2.LOW)
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

def main():
  setupGlobalPins()
  setupESC(ESC1PIN)
  setupESC(ESC2PIN)
  setupESC(ESC3PIN)
  setupESC(ESC4PIN)

if __name__ == '__main__':
  main()
