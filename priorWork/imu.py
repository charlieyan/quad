#this class opens an interface for the 6DOF IMU
#specifically it 
#1. maintains a set of booleans for states of the orientation 
#   such as is<Un|>Stable, statusX, statusY, statusZ
#   and caller can wait on these things to happen
#2. lets the caller define what IS "stable", allowing for holding orientations
#3. set tolerances: how exact do we want to be with regards to orientation?
import Adafruit_BBIO.GPIO as GPIO

import time
import sys
 
class IMU:
  #constants
  IMU_5HZ = 1

  #tolerance levels
  IMU_MOST_TOLERANT = 0

  #constructor
  def __init__(self):
    self.updateRate = IMU_5HZ #how often to take readings from hardware
    self.toleranceLevel = IMU_MOST_TOLERANT
    # parameters for circular buffers for X, Y, Z
    self.xCircularBufferLength = 10;
    self.yCircularBufferLength = 10;
    self.zCircularBufferLength = 10;

  def setStable(x,y,z):
    return

  #api level 0: imu primitives: regarding the data from the IMU
  def 

  #api level 1: higher primitives: regarding events, and caller definitions
