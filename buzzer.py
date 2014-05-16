import Adafruit_BBIO.GPIO as GPIO

# FUNCTIONS
def setGlobals():
  global BUZZERPIN
  BUZZERPIN = "P9_12"

setGlobals()

GPIO.setup(BUZZERPIN, GPIO.OUT)
GPIO.output(BUZZERPIN, GPIO.HIGH)
GPIO.cleanup()