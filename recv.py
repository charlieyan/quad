from nrf24 import NRF24
import Adafruit_BBIO.GPIO as GPIO
import time

CMD = 0
MOT1 = 2
MOT2 = 4
MOT3 = 6
MOT4 = 8
def parseCmd(contents):
  print contents[CMD]
  return 

#set notification pin P9_36
GPIO.setup("P9_41", GPIO.OUT)
GPIO.output("P9_41", GPIO.HIGH)

radio = NRF24()
radio.begin(2,0, "P9_27", "P9_32")
radio.setChannel(76)
#radio.setRetries(15,15)
radio.setPayloadSize(10)
radio.setDataRate(NRF24.BR_1MBPS)
radio.setPALevel(NRF24.PA_MIN)

#print details
print radio.getChannel()
print radio.getPayloadSize()
print radio.getPALevel()
print radio.getDataRate()
print radio.getCRCLength()

# open up listening
radio.openReadingPipe(1, [0xc2, 0xc2, 0xc2, 0xc2, 0xc2])
radio.startListening()

while True:
  pipe = [0]
  while not radio.available(pipe):
    #time.sleep(0.01)
    time.sleep(0.5)
    print "no radio\n"
  recv_buffer = []
  radio.read(recv_buffer)
  parseCmd(recv_buffer)
  print recv_buffer
  #time.sleep(0.01)
  time.sleep(0.5)

GPIO.cleanup()
