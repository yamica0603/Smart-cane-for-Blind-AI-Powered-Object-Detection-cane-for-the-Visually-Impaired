import RPi.GPIO as GPIO
import time
import pyttsx3
engine = pyttsx3.init()
GPIO.setmode(GPIO.BCM)

TRIG = 23 
ECHO = 24
while 1:

    GPIO.setmode(GPIO.BCM)
    print ("Distance Measurement In Progress")
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)

    GPIO.output(TRIG, False)
    print ("Waiting For Sensor To Settle")
    time.sleep(2)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    print ("Distance:",distance,"cm")
    if distance <= 100:
        
        engine.say("Alert")
        engine.runAndWait()
        time.sleep(2)
    GPIO.cleanup()
