#include <Streaming.h>
#include <MsTimer2.h>

#define CUPSENSE A0
#define JACKW A1
#define TEQW A2
#define GINW A3
#define MIXW A4
#define JACK 4
#define TEQUILA 7
#define GINGER 8
#define MIX 12
#define POUR 200

bool cup = false, pour = false;
int jackWeight, teqWeight, gingWeight, mixWeight, liquor, mixer;

void setup(){
  Serial.begin(57600);
  MsTimer2::set(10, isCup);
  //getWeights();
  pinMode(JACK, OUTPUT);
  pinMode(TEQUILA, OUTPUT);
  pinMode(GINGER, OUTPUT);
  pinMode(MIX, OUTPUT);
  MsTimer2::start();
}

void loop(){
  while(!Serial.available());
  char cmd = Serial.read();
  if(cmd == 'J'){
    digitalWrite(JACK, HIGH);
    digitalWrite(TEQUILA, HIGH);
    delay(5000);
    digitalWrite(JACK, LOW);
    digitalWrite(TEQUILA, LOW);
    Serial << "done" << endl;
  }
}

void isCup(){
  int sense = analogRead(CUPSENSE);
  //Serial << sense << endl;
  if(sense <= 400 && pour){
    cup = false;
    digitalWrite(JACK, LOW);
    digitalWrite(TEQUILA, LOW);
    digitalWrite(GINGER, LOW);
    digitalWrite(MIX, LOW);
    Serial << "CUP REMOVED" << endl;
  }
  else if(sense <= 400 && !pour){
    cup = false;
  }
  else{
    cup = true;
  }
}

/*
void getWeights(){
  jackWeight = analogRead(JACKW);
  teqWeight = analogRead(TEQW);
  gingWeight = analogRead(GINW);
  mixWeight = analogRead(MIX);
}

void jackGinger(){
  pour = true;
  liquor = jackWeight;
  mixer = gingWeight;
  if(cup){
    digitalWrite(JACK, HIGH);
    digitalWrite(GINGER, HIGH);
    while(cup && pour){
     getWeights();
     if(liquor - jackWeight == POUR){
      digitalWrite(JACK, LOW); 
    }
    if(mixer - gingWeight == 2 * POUR){
      digitalWrite(GINGER, LOW);
      Serial << "jackGinger Done" << endl;
      pour = false; 
    }
   }
  }
  else{
    Serial << "Cup not present" << endl;
  }
}
*/
