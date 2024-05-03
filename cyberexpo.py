import pineworkslabs.RPi as GPIO
import time
trigPin = 27
echoPin = 26
vibrationPin = 18

trigPin2 = 22
echoPin2 = 23
vibrationPin2 = 21

GPIO.setmode(GPIO.LE_POTATO_LOOKUP)

GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(vibrationPin, GPIO.OUT)

GPIO.setup(trigPin2, GPIO.OUT)
GPIO.setup(echoPin2, GPIO.IN)
GPIO.setup(vibrationPin2, GPIO.OUT)

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
        distance = distance_measurement()
        if distance < 10:
            GPIO.output(vibrationPin, GPIO.HIGH)
        else:
            GPIO.output(vibrationPin, GPIO.LOW)
        time.sleep(0.1)
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
