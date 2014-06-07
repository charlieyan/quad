from Adafruit_I2C import *
import time

addr = 0x40
i2c = Adafruit_I2C(addr)
i2c.write8(0x0,0x0)

#attempt to set the frequency for i2c
prescale = 100.0

#set the SLEEP bit of MODE1 register set to 1
SLEEPBIT = 4
MODE1VAL = 1 << SLEEPBIT
i2c.write8(0x0,MODE1VAL)
i2c.write8(254,99)

#set pwm: 16 ON_L, OFF_L, OFF_H
x = 0x6+4*4

i = 150
i2c.write8(x,0)
i2c.write8(x+1,0)
i2c.write8(x+2,i2c.reverseByteOrder(i))
i2c.write8(x+3,0)

time.sleep(2)
i2c.write8(0x0,0x0)
