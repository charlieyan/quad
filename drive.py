from bbio import *

def setup():
  """ This will be called once before the main loop. """

def loop():
  """ This is the main loop of your program. It will be called repeatedly
      until ctrl-c is pressed, or stop() is called from within. """

# We then pass the two functions to run() to start the program:
run(setup, main)