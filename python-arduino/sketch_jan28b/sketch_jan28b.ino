int led=13;
int opcion;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(led,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    opcion=Serial.read();
    if(opcion=='p'){
      digitalWrite(led,HIGH);
    }
    else if(opcion=='n'){
      digitalWrite(led,LOW);
    }
  }
}
