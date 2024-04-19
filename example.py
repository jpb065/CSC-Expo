import serial
import time

# Establish serial connection
ser = serial.Serial('COM4', 9600) # Replace 'COM3' with the appropriate port name
time.sleep(2) # Allow some time for the connection to establish

# Send commands to Arduino
ser.write(b'1') # Send command 1
response = ser.readline().decode().strip()
print("Arduino response:", response)

ser.write(b'2') # Send command 2
response = ser.readline().decode().strip()
print("Arduino response:", response)

# Close the serial connection
ser.close()