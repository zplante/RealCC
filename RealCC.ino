/*

*/
const int motorpin=6;

String trigger;

void setup() {
    pinMode(motorpin,OUTPUT);
    digitalWrite(motorpin,HIGH);
    Serial.begin(9600);
    Serial.setTimeout(10);
}

void loop() {
    trigger= Serial.readString();
    if(trigger.length() >0){
    digitalWrite(motorpin,LOW);
    delay(50);
    digitalWrite(motorpin,HIGH);
  }
}
