#define IN_1 D7
#define IN_2 D6

void setup() {
  pinMode(IN_1, OUTPUT);
  pinMode(IN_2, OUTPUT);
}
void loop() {
  digitalWrite(IN_2, LOW);

  for(int i=0; i<256; i++) {
    analogWrite(IN_1, i);
    delay(10);
  }
  for(int i=0; i<256; i++) {
    analogWrite(IN_1, 0xff - i);
    delay(10);
  }

  digitalWrite(IN_1, LOW);
  
  for(int i = 0; i<256; i++) {
    analogWrite(IN_1, i);
    delay(10);
  }
  for(int i = 0; i<256; i++) {
    analogWrite(IN_1, 0xff - i);
    delay(10);
  }
}
