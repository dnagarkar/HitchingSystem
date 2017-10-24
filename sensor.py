import RPi.GPIO as GPIO
import time
import math

GPIO.setmode(GPIO.BCM)

TRIG_LEFT = 23
ECHO_LEFT = 24
TRIG_RIGHT = 17
ECHO_RIGHT = 27  
ERROR = 1

GPIO.setup(TRIG_LEFT, GPIO.OUT)
GPIO.setup(ECHO_LEFT, GPIO.IN)

GPIO.setup(TRIG_RIGHT, GPIO.OUT)
GPIO.setup(ECHO_RIGHT, GPIO.IN)

def distance(GPIO_TRIGGER, GPIO_ECHO):
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance


DIST_LEFT = distance(TRIG_LEFT, ECHO_LEFT)
DIST_RIGHT = distance(TRIG_RIGHT, ECHO_RIGHT)

if(math.abs(DIST_LEFT - DIST_RIGHT) <= error):
    print "move forward"
else if(DIST_LEFT <= DIST_RIGHT + error):
    print "“turn left”"
else:
    print "“turn right”"
