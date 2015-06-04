// in this iteration, we connect to the quad via BLE
// through BLE, we set 'throttle' for short durations of time to 'get air'

#include <SPI.h>
#include <Servo.h> 
#include "Adafruit_BLE_UART.h"

// connect CLK/MISO/MOSI to hardware SPI
// e.g. On UNO & compatible: CLK = 13, MISO = 12, MOSI = 11
#define ADAFRUITBLE_REQ 10
#define ADAFRUITBLE_RDY 2     // This should be an interrupt pin, on Uno thats #2 or #3
#define ADAFRUITBLE_RST 9

Adafruit_BLE_UART BTLEserial = Adafruit_BLE_UART(ADAFRUITBLE_REQ, ADAFRUITBLE_RDY, ADAFRUITBLE_RST);
aci_evt_opcode_t laststatus = ACI_EVT_DISCONNECTED;

// 4 escs
Servo esc1; int escPin1 = 8;
Servo esc2; int escPin2 = 6;
Servo esc3; int escPin3 = 3;
Servo esc4; int escPin4 = 5;


Servo escs[] = {esc1, esc2, esc3, esc4};
int escPin[] = {escPin1, escPin2, escPin3, escPin4};

// min and max pulse
int minPulseRate        = 1000; // 1 second min pulse width
int maxPulseRate        = 2000; // 2 second max pulse width
int throttleChangeDelay = 50; // delay 50 microseconds
int spinLowerBound      = 20; // motors spin at around 20
int stepSize            = 5;
int airTimeMilli        = 3000;

// buzzer config
int buzzerPin1 = 7;
int duration = 20;
int pause = 50;

void setup() {  
  BTLEserial.setDeviceName("QUAD"); /* 7 characters max! */
  BTLEserial.begin();
 
  initEscs();
  
  // buzzer
  pinMode(buzzerPin1, OUTPUT);
  digitalWrite(buzzerPin1, LOW);
}

void loop() {
  BTLEserial.pollACI();
  aci_evt_opcode_t status = BTLEserial.getState();
  if (status != laststatus) {
    if (status == ACI_EVT_DEVICE_STARTED) {
      //Serial.println(F("* Advertising started"));
      doBeepN(buzzerPin1, duration, pause, 1);
    }
    if (status == ACI_EVT_CONNECTED) {
      //Serial.println(F("* Connected!"));
      doBeepN(buzzerPin1, duration, pause, 2);
    }
    if (status == ACI_EVT_DISCONNECTED) {
      //Serial.println(F("* Disconnected or advertising timed out"));
      doBeepN(buzzerPin1, duration*40, pause, 1);
    }
    laststatus = status;
  }
  
  if (status == ACI_EVT_CONNECTED && laststatus == ACI_EVT_CONNECTED) {
    String bleString = String("");
    while (BTLEserial.available()) {
      char c = BTLEserial.read();
      bleString = bleString + c;
    }
    
    if (bleString.charAt(0) == 'S') {
      // adjust stepSize
      String temp = bleString.substring(1);
      int newStepSize = temp.toInt();
      if (newStepSize > 1 && newStepSize < 40) {
         stepSize = newStepSize;
        doBeepN(buzzerPin1, duration, pause, 6);
      }
      else {
        stepSize = 1; 
      }
    }
    else if (bleString.charAt(0) == 'D') {
      // adjust duration
      String temp = bleString.substring(1);
      int newAirTime = temp.toInt()*1000;
      if (newAirTime > 3000 && newAirTime < 9000) { // max of 10 seconds allowed
         airTimeMilli = newAirTime;
      }
      else {
        airTimeMilli = 3000; 
      }
    }
    else {
      // assume bleString is number
      int bleInt = bleString.toInt();
      int throttle = normalizeThrottle(bleInt);
    
      if (throttle > 0) {
        changeThrottle(throttle, stepSize);
        delay(airTimeMilli); // 3 second kill cycle
        doBeepN(buzzerPin1, duration, pause, 1);
        changeThrottle(0, stepSize);
      }
      
      //Serial.print(c); // u or d, increment by 10
      if (bleString == "uu") {
        doBeepN(buzzerPin1, duration, pause, 3);
      }
      else if (bleString == "dd") {
        doBeepN(buzzerPin1, duration, pause, 4);
      }
    }
  }
}

//Change throttle value
void changeThrottle(int throttle, int upStep) {
  int currentThrottle = readThrottle();
  
  int step = upStep; // THIS IS INCREDIBLY IMPORTANT FOR FLYING
  if(throttle < currentThrottle) {
    step = -1;
  }
  
  // Slowly move to the new throttle value
  while(currentThrottle != throttle) {
    int newVal = currentThrottle + step;
    if (newVal < throttle) {
      newVal = throttle;
    }
    if (newVal > throttle) {
      newVal = throttle; 
    }
    writeTo4Escs(newVal);
    
    currentThrottle = readThrottle();
    delay(throttleChangeDelay);
  }
}
 
//Read the throttle value
int readThrottle() {
  int throttle = esc1.read();
  return throttle;
}
 
//Change velocity of the 4 escs at the same time
void writeTo4Escs(int throttle) {
  /*int throttle2 = throttle - 7;
  if (throttle2 < 0) {
    throttle2 = 0;
  }*/
  esc1.write(throttle);
  esc2.write(throttle);
  esc3.write(throttle);
  esc4.write(throttle);
}
 
//Init escs
void initEscs() {
  esc1.attach(escPin1, minPulseRate, maxPulseRate);
  esc2.attach(escPin2, minPulseRate, maxPulseRate);
  esc3.attach(escPin3, minPulseRate, maxPulseRate);
  esc4.attach(escPin4, minPulseRate, maxPulseRate);
  
  //Init motors with 0 value
  writeTo4Escs(0);
}
 
// start the motors
void startUpMotors() {
  writeTo4Escs(spinLowerBound);
}
 
// ensure the throttle value is between 0 - 180
int normalizeThrottle(int value) {
  if(value < 0) {
    return 0;
    
  } else if(value > 180) { // use 180
    return 180;
  }
  return value;
}

void doBeepN(int pinNumber, int duration, int pause, int n) {
  for (int i = 0; i < n; i++) {
    doBeep(buzzerPin1, duration);
    delay(pause);
  } 
}

void doBeep(int pinNumber, int duration) {
  digitalWrite(pinNumber, HIGH);
  delay(duration);
  digitalWrite(pinNumber, LOW);
}
