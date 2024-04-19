#include <Arduino.h>

void setup() {
  Serial.begin(9600); // Initialize serial communication
}

void loop() {
  if (Serial.available() > 0) { // Check if data is available to read
    char command = Serial.read(); // Read the incoming byte
    // Perform actions based on the command
    if (command == '1') {
      // Do something
      Serial.println("Command 1 executed");
    } else if (command == '2') {
      // Do something else
      Serial.println("Command 2 executed");
    }
  }
}
