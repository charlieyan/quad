#!/bin/sh
LEDDIR="/sys/class/leds/beaglebone:green:usr"

L1=$1
led1=$LEDDIR$L1

current=$(pwd)
cd $led1 && echo none > trigger && echo $2 > brightness
cd $current
