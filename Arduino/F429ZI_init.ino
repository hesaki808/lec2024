// https://scrapbox.io/ArduinoSTM32/HardwareTimer
// https://github.com/stm32duino/Arduino_Core_STM32/blob/main/variants/STM32F4xx/F427Z(G-I)T_F429ZET_F429Z(G-I)(T-Y)_F437Z(G-I)T_F439Z(G-I)(T-Y)/variant_NUCLEO_F4x9ZI.cpp

#include <Wire.h>
#include <LwIP.h>
#include <STM32Ethernet.h>

EthernetClient client;
HardwareTimer *MyTimer = new HardwareTimer (TIM2);

void setup() {  
  Serial.begin(9600);
  while (!Serial) {;}

  MyTimer->pause();
  MyTimer->setPrescaleFactor(16800); // 168MHz
  MyTimer->setOverflow(1, HERTZ_FORMAT);
  MyTimer->attachInterrupt(intDHCP);
  MyTimer->refresh();
  MyTimer->resume();

  if (Ethernet.begin() == 0) {
    Serial.println("Ethernet fail.");
    for (;;)
      ;
  }
  else {
    Serial.println("Ethernet ok.");
  }
  printIPAddress();
}

void loop() {
   delay(500);
}

void printIPAddress()
{
  Serial.print("My IP address: ");
  for (byte thisByte = 0; thisByte < 4; thisByte++) {
    Serial.print(Ethernet.localIP()[thisByte], DEC);
    Serial.print(".");
  }
  Serial.println();
}

void intDHCP(void) {
    switch (Ethernet.maintain()) {
    case 1:
      Serial.println("Renew fail.");
      break;
    case 2:
      Serial.println("Renew success.");
      printIPAddress();
      break;
    case 3:
      Serial.println("Rebind fail.");
      break;
    case 4:
      Serial.println("Rebind success.");
      printIPAddress();
      break;
    default:
      Serial.println("continue.");
      break;
  }
}


