// PB14:RED, PB0:GREEN, PB7:BLUE
// PC13:USER_BUTTON

int ledPin_R = PB14;   // LED R
int ledPin_G = PB0;    // LED G
int ledPin_B = PB7;    // LED B

void setup() {
  pinMode(ledPin_R,OUTPUT);
  pinMode(ledPin_G,OUTPUT);
  pinMode(ledPin_B,OUTPUT);
}

void loop() {

    digitalWrite(ledPin_R, HIGH);
    digitalWrite(ledPin_G, HIGH);
    digitalWrite(ledPin_B, HIGH);
    delay(500);
    digitalWrite(ledPin_R, LOW);
    digitalWrite(ledPin_G, LOW);
    digitalWrite(ledPin_B, LOW);
    delay(500);
}
