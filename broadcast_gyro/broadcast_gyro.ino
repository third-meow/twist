#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

Adafruit_BNO055 bno055 = Adafruit_BNO055(19, 0x29);
imu::Vector<3> gyro_data;

long long last_time = 0;

void setup() {
  while(!bno055.begin()) delay(20);
	Serial.begin(9600);
}


void loop() {
	// wait for 1 milli second
	while(micros() < last_time + 1000) {;}
	last_time = micros();


	// print gyro data to serial at 100Hz
	gyro_data = bno055.getVector(Adafruit_BNO055::VECTOR_GYROSCOPE);
	Serial.print(gyro_data.x());
	Serial.print(", ");
	Serial.print(gyro_data.y());
	Serial.print(", ");
	Serial.print(gyro_data.z());
	Serial.println();
}

