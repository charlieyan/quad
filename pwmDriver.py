from Adafruit_I2C import *
import math
import time

class PWMDriver:
  PCA9685_SUBADR1 = 0x2
  PCA9685_SUBADR2 = 0x3
  PCA9685_SUBADR3 = 0x4
  
  PCA9685_MODE1 = 0x0
  PCA9685_PRESCALE = 0xFE

  LED0_ON_L = 0x6
  LED0_ON_H = 0x7
  LED0_OFF_L = 0x8
  LED0_OFF_H = 0x9

  ALLLED_ON_L = 0xFA
  ALLLED_ON_H = 0xFB
  ALLLED_OFF_L = 0xFC
  ALLLED_OFF_H = 0xFD
  
  SERVOMIN = 150
  SERVOMAX = 600

  def __init__(self, addr, freq):
    self.i2caddr = addr
    self.servonum = 0
    self.freq = freq
    self.i2c = Adafruit_I2C(addr)
    self.begin()
    self.setPWMFreq(freq)

  def setServoPulse(n, pulse):
    pulseLength = 1000000
    pulseLength /= 60
    print str(pulseLength) + " us per period"
    pulseLength /= 4096
    print str(pulseLength) + " us per bit"
    pulse *= 1000
    pulse /= pulseLength
    print "pulse: " + str(pulse)
    pwm.setPWM(n, 0, pulse)
 
  def begin(self):
    self.reset()

  def reset(self):
    self.i2c.write8(self.PCA9685_MODE1,0x0)
 
  def write8(self, addr, d):
    print "write8 on " + str(addr) + " value " + str(d)
    self.i2c.write8(int(addr),int(d))
  
  def write16(self, addr, value):
    self.i2c.write16(addr, value)

  def writeList(self, addr, dataList):
    self.i2c.writeList(addr, dataList)

  def readU8(self, addr):
    return self.i2c.readU8(addr)

  def readU16(self, addr):
    return self.i2c.readU16(addr)
  
  def readU16Rev(self, addr):
    return self.i2c.readU16Rev(addr)

  def readS8(self, addr):
    return self.i2c.readS8(addr)

  def readS16(self, addr):
    return self.i2c.readS16(addr)

  def readS16Rev(self, addr):
    return self.i2c.readS16Rev(addr)

  def readList(self, addr, length):
    return self.i2c.readList(addr, length)

  def reverseByteOrder(self, data):
    return self.i2c.reverseByteOrder(data)

  def setPWM(self, num, on, off):
    self.i2c.write8(self.i2caddr,self.LED0_ON_L+4*num)
    self.i2c.write8(self.i2caddr,on)
    self.i2c.write8(self.i2caddr,on>>8)
    self.i2c.write8(self.i2caddr,off)
    self.i2c.write8(self.i2caddr,off>>8)

  def setPWMFreq(self, freq):
    prescaleval = 25000000
    prescaleval /= 4096
    prescaleval /= freq
    prescaleval -= 1
    print "Estimated pre-scale: " + str(prescaleval)
    prescale = math.floor(prescaleval + -0.5)
    print "Final pre-scale: " + str(prescale)
   
    oldmode = self.readU8(self.PCA9685_MODE1)
    newmode = oldmode & 0x7F | 0x10
    self.write8(self.PCA9685_MODE1, newmode)
    self.write8(self.PCA9685_PRESCALE, prescale)
    self.write8(self.PCA9685_MODE1, oldmode)
    time.sleep(5/1000)
    self.write8(self.PCA9685_MODE1, oldmode | 0xa1)    
