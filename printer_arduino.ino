#include <Servo.h>

Servo Y;

String dane;
int correction;

#define stepPinZ 3
#define dirPinZ 2
#define stepPinX 5
#define dirPinX 4

int moveY() {
  Y.write(20);
  delay(300);
  Y.write(60);
}

int moveX() {
  if (correction == 1) {
    for(int i = 0; i < 11; i++) {
      digitalWrite(stepPinX, HIGH);
      delay(5);
      digitalWrite(stepPinX, LOW);
      delay(5);
    }
  }
  else {
    for(int i = 0; i < 10; i++) {
      digitalWrite(stepPinX, HIGH);
      delay(5);
      digitalWrite(stepPinX, LOW);
      delay(5);
    }
  }
  }

int moveZ() {
    for(int i = 0; i < 10; i++) {
      digitalWrite(stepPinZ, HIGH);
      delay(5);
      digitalWrite(stepPinZ, LOW);
      delay(5);
    }
}

void setup() {
 Serial.begin(115200);
 Serial.setTimeout(0.1);
 pinMode(stepPinZ, OUTPUT);
 pinMode(dirPinZ, OUTPUT);
 pinMode(stepPinX, OUTPUT);
 pinMode(dirPinX, OUTPUT);
 Y.attach(11);
 Y.write(60);
 digitalWrite(dirPinX, LOW);
 digitalWrite(dirPinZ, LOW);
 correction = 1;
}

void loop() {
  while (!Serial.available());
  dane = Serial.readString();
  Serial.print(dane);

  if (dane == "1") {
    moveY();
  }
  else if (dane == "2") {
    moveZ();
  }
  else if (dane == "3") {
    moveX();
  }
  else if (dane == "4") {
    digitalWrite(dirPinX, LOW);
    correction = 1;
  }
  else if (dane == "5") {
    digitalWrite(dirPinX, HIGH);
    correction = 0;
  }
}
