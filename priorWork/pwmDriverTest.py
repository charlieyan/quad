from pwmDriver import PWMDriver

SERVOMIN = 150
SERVOMAX = 600

servonum = 4
driver = PWMDriver(0x40,60)
for pulselen in range(SERVOMIN, SERVOMAX):
  driver.setPWM(servonum, 4)
