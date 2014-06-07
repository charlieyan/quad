#usage: sudo -u root python recv.py 0.5
#make sure you run the once_ ....sh before running this
import os
import time
import sys
from nrf24 import NRF24
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
from Adafruit_I2C import *
from pwmDriver import PWMDriver

#NRF
SPIMAJOR = 1
SPIMINOR = 0
NRFCHANNEL = 76

CMD = 0
MOT1 = 2
MOT1X = 3
MOT2 = 4
MOT2X = 5
MOT3 = 6
MOT4 = 8
RESTSPEED = 4

#CMDS
#LEVEL 0 API CMDS: <esc primitives> this is the level concerning ESC speeds
REST = 1
ALLSET = 2
ONESET = 3

#LEVEL 1 API CMDS: <movement primitives> built atop esc primitives
MOVE   = 4 #move <left, right, forward and back>
ALT    = 5 #altitude <rise or fall>

#FUNCTIONS
def debugMsg(msg):
  if debug:
    print msg  

def toggleSysLED(led, state):
  #led = [0,1,2,3], state = 0/1
  os.system("sudo /home/ubuntu/quad/util/set.sh " + str(led) + " " + str(state))

def printNRFDetails():
  #print details, these must match what the transmitter is putting out
  print radio.getChannel()
  print radio.getPayloadSize()
  print radio.getPALevel()
  print radio.getDataRate()
  print radio.getCRCLength()

def setGlobals():
  global ESC1PIN
  global ESC2PIN 
  global ESC3PIN 
  global ESC4PIN
  ESC1PIN = "P8_13"
  ESC2PIN = "P9_16"
  ESC3PIN = "P9_21"
  ESC4PIN = "P9_42"
  global RECVPIN 
  global CEPIN
  global IRQPIN
  CEPIN   = "P9_27"
  IRQPIN  = "P9_32"

def armESCs(escList):
  for esc in escList:
    PWM.start(esc, 4, 50)

def parseCmd(contents,escList,latest):
  cmd = contents[CMD]
  if ((cmd == latest) or (cmd == None)):
    debugMsg("nothing to do")
    return latest
  toggleSysLED(1,1)
  if cmd == REST:
    # put quad at rest <1, 0, 0, 0, 0...>
    print "putting quad to rest"
    for esc in escList:
      PWM.set_duty_cycle(esc, float(RESTSPEED))
  elif cmd == ALLSET:
    # put all motors at same speed <2, 0, 6, 3, 0> = 6.3
    speed = float(str(contents[MOT1]) + "." + str(contents[MOT1X]))
    print "putting all motors at the same speed: " + str(speed)
    for esc in escList:
      PWM.set_duty_cycle(esc, speed)
  elif cmd == ONESET:
    # update motors individually <3, 0, 1, 0, 6, 6> => sets motor on ESC1 to 6.6
    esc = escList[contents[MOT1]-1]
    speed = float(str(contents[MOT2]) + "." + str(contents[MOT2X]))
    print "putting esc at " + esc + " at speed: " + str(speed)
    PWM.set_duty_cycle(esc, speed)
  time.sleep(0.5)
  toggleSysLED(1,0)
  return cmd

#MAIN SCRIPT
setGlobals()
escList = [ESC1PIN, ESC2PIN, ESC3PIN, ESC4PIN]
armESCs(escList)
latest = 0

#get command arguments
recvDelay = float(sys.argv[1]) # how much time between reading from transmitter
debug = (int(sys.argv[2]) == 1)

radio = NRF24()
radio.begin(SPIMAJOR, SPIMINOR, CEPIN, IRQPIN) #must be 2,0, plug into SPI0 ones
radio.setChannel(NRFCHANNEL)
radio.setPayloadSize(10)
radio.setDataRate(NRF24.BR_1MBPS)
radio.setPALevel(NRF24.PA_MIN)

if debug:
  printNRFDetails()
  radio.printDetails()

#open up listening
readingPipe = [0xc2, 0xc2, 0xc2, 0xc2, 0xc2]
radio.openReadingPipe(1, readingPipe)
radio.startListening()

while True:
  pipe = [0]
  while not radio.available(pipe):
    time.sleep(recvDelay)
    debugMsg("no radio")
    latest = parseCmd([1,0,0,0],escList,latest)
  recv_buffer = []
  radio.read(recv_buffer)
  latest = parseCmd(recv_buffer,escList, latest)
  debugMsg(recv_buffer)
  time.sleep(recvDelay)

GPIO.cleanup()
