import pineworkslabs.RPi as GPIO
import time
trigPin = 27
echoPin = 26
vibrationPin = 20

trigPin2 = 22
echoPin2 = 23
vibrationPin2 = 21

sensitivity = 61

switches = [ 16,13,12,6 ]

GPIO.setmode(GPIO.LE_POTATO_LOOKUP)

GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(vibrationPin, GPIO.OUT)

GPIO.setup(trigPin2, GPIO.OUT)
GPIO.setup(echoPin2, GPIO.IN)
GPIO.setup(vibrationPin2, GPIO.OUT)

for switch in switches:
    GPIO.setup(switch, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def change_sensitivity(val):
    if val == 0:
        return 10
    elif val == 1:
        return 30
    elif val == 2:
        return 50
    elif val == 3:
        return 100
    else:
        return 60 #just in case something weird happens
    
        

def distance_measurement():
    GPIO.output(trigPin, GPIO.LOW)
    time.sleep(0.000002)
    GPIO.output(trigPin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trigPin, GPIO.LOW)

    pulse_start = time.time()
    pulse_end = time.time()
    
    while GPIO.input(echoPin) == GPIO.LOW:
        pulse_start = time.time()

    while GPIO.input(echoPin) == GPIO.HIGH:
        pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150
    return distance

def distance_measurement2():
    GPIO.output(trigPin2, GPIO.LOW)
    time.sleep(0.000002)
    GPIO.output(trigPin2, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trigPin2, GPIO.LOW)

    pulse_start = time.time()
    pulse_end = time.time()
    
    while GPIO.input(echoPin2) == GPIO.LOW:
        pulse_start = time.time()

    while GPIO.input(echoPin2) == GPIO.HIGH:
        pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start

    distance2 = pulse_duration * 17150
    return distance2
    
try:
    while True:
        if (GPIO.input(16) == GPIO.HIGH):
            sensitivity = change_sensitivity(0)
            print(f"Sensitivity Changed To: {sensitivity} cm")
        if (GPIO.input(13) == GPIO.HIGH):
            sensitivity = change_sensitivity(1)
            print(f"Sensitivity Changed To: {sensitivity} cm")
        if (GPIO.input(12) == GPIO.HIGH):
            sensitivity = change_sensitivity(2)
            print(f"Sensitivity Changed To: {sensitivity} cm")
        if (GPIO.input(6) == GPIO.HIGH):
            sensitivity = change_sensitivity(3)
            print(f"Sensitivity Changed To: {sensitivity} cm")
        distance = distance_measurement()
        if distance < sensitivity:
            GPIO.output(vibrationPin, GPIO.HIGH)
        else:
            GPIO.output(vibrationPin, GPIO.LOW)
        time.sleep(0.3)
        distance2 = distance_measurement2()
        if distance2 < 10:
            GPIO.output(vibrationPin2, GPIO.HIGH)
        else:
            GPIO.output(vibrationPin2, GPIO.LOW)
        print("Distance: {:.2f} cm\tDistance 2: {:.2f} cm".format(distance, distance2))
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Measurement stopped by user")
    GPIO.cleanup()
