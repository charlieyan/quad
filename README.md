quad
====

Various attempts to control a quadcopter

Current approach:
====
Arduino / Bluetooth with code taken from https://github.com/charlieyan/BlueCopter
Mojo v3 board with onboard camera

Roadmap:
====
1. get bluecopter project to work
2. add HMC5883 magnetometer and BMP085 chips integrated, contribute back
3. replace RX component with bluetooth / xbee / otg and write companion program
4. port bluecopter code in 1. to mojo v3
5. add mojo v3 camera project

Past approaches:
====
BeagleBone Black / Ubuntu Quadcopter Project
NRF24L01+ code taken from https://github.com/jpbarraca/pynrf24