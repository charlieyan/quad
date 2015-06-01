/* YourDuinoStarter Example: nRF24L01 Transmit Joystick values
 - WHAT IT DOES: Reads Analog values on A0, A1 and transmits
   them over a nRF24L01 Radio Link to another transceiver.
 - SEE the comments after "//" on each line below
 - CONNECTIONS: nRF24L01 Modules See:
 http://arduino-info.wikispaces.com/Nrf24L01-2.4GHz-HowTo
   1 - GND
   2 - VCC 3.3V !!! NOT 5V
   3 - CE to Arduino pin 9
   4 - CSN to Arduino pin 10
   5 - SCK to Arduino pin 13
   6 - MOSI to Arduino pin 11
   7 - MISO to Arduino pin 12
   8 - UNUSED

/*-----( Import needed libraries )-----*/
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
/*-----( Declare Constants and Pin Numbers )-----*/
#define CE_PIN   9
#define CSN_PIN 10

// NOTE: the "LL" at the end of the constant is "LongLong" type
const uint64_t pipe = 0xc2c2c2c2c2LL; // Define the transmit pipe, must be the same as receiving pipe

/*-----( Declare objects )-----*/
RF24 radio(CE_PIN, CSN_PIN); // Create a Radio
/*-----( Declare Variables )-----*/
int commmands[5];  // 5 bytes: CMD, MOTOR1, MOTOR2, MOTOR3, MOTOR4

char serialinput;

void setup()   /****** SETUP: RUNS ONCE ******/
{
  Serial.begin(9600);
  radio.begin();
  radio.setPayloadSize(10);
  radio.setDataRate(RF24_1MBPS);
  radio.setPALevel(RF24_PA_MIN);
  radio.openWritingPipe(pipe);
  Serial.println(radio.getChannel());
  Serial.println(radio.getPayloadSize());
  Serial.println(radio.getPALevel());
  Serial.println(radio.getDataRate());
  Serial.println(radio.getCRCLength());
}//--(end setup )---

void go() {
  // reset
  commmands[0] = 1; //2 bytes max, CMD 1,3,10 ALLSET: 1, 5
  commmands[1] = 0; //2 bytes max, MOT1 6, 9, 11
  commmands[2] = 0; //2 bytes max, MOT2
  commmands[3] = 0; //2 bytes max, MOT3M
  commmands[4] = 0; //2 bytes max, MOT4
  radio.write( commmands, sizeof(commmands) );
  delay(1000);
  
  commmands[0] = 5; //2 bytes max, CMD 1,3,10 ALLSET: 1, 5
  commmands[1] = 9; //2 bytes max, MOT1 6, 9, 11
  commmands[2] = 0; //2 bytes max, MOT2
  commmands[3] = 0; //2 bytes max, MOT3
  commmands[4] = 0; //2 bytes max, MOT4
  radio.write( commmands, sizeof(commmands) );
  
}
void loop()   /****** LOOP: RUNS CONSTANTLY ******/
{
  /*
  send 2 bytes max, 255, receiver takes it in 16 bit lengths
  0[255, 255], 1[255, 255] ->
  CMDs = [NOP, REST, FLY], NOP will cause it to beep
  MOTOR# = speed
  */
  // send data only when you receive data:
//  if (Serial.available() > 0) {
//            // read the incoming byte:
//            serialinput = Serial.read();
//
//            if (serialinput == 'go')
//            {
//              Serial.println("going to go! stand back!");
//              //go();
//            }
//    }
  
  commmands[0] = 1; //2 bytes max, CMD 1,3,10 ALLSET: 1, 5
  commmands[1] = 0; //2 bytes max, MOT1 6, 9, 11
  commmands[2] = 0; //2 bytes max, MOT2
  commmands[3] = 0; //2 bytes max, MOT3M
  commmands[4] = 0; //2 bytes max, MOT4
  radio.write( commmands, sizeof(commmands) );
  delay(1000);
  
//  commmands[0] = 5; //2 bytes max, CMD 1,3,10 ALLSET: 1, 5
//  commmands[1] = 9; //2 bytes max, MOT1 6, 9, 11
//  commmands[2] = 0; //2 bytes max, MOT2
//  commmands[3] = 0; //2 bytes max, MOT3
//  commmands[4] = 0; //2 bytes max, MOT4
//  radio.write( commmands, sizeof(commmands) );
  
  delay(500);
}//--(end main loop )---

/*-----( Declare User-written Functions )-----*/

//NONE
//*********( THE END )***********
