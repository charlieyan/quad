from Adafruit_I2C import Adafruit_I2C

class PWMDriver:
  PCA9685_SUBADR1 0x2
  PCA9685_SUBADR2 0x3
  PCA9685_SUBADR3 0x4
  
  PCA9685_MODE1 0x0
  PCA9685_PRESCALE 0xFE

  LED0_ON_L 0x6
  LED0_ON_H 0x7
  LED0_OFF_L 0x8
  LED0_OFF_H 0x9

  ALLLED_ON_L 0xFA
  ALLLED_ON_H 0xFB
  ALLLED_OFF_L 0xFC
  ALLLED_OFF_H 0xFD

  def __init__(self, addr):
    self.i2caddr = addr
    self.i2c = Adafruit_I2C(addr)

  def begin(self):
    reset()

  def reset(self):
    i2c.write8(PCA9685_MODE1,0x0)