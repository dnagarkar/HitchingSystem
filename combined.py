import sys, pygame
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

def moveright(baler_rect):
  #move baler left
  baler_rect= baler_rect.move([-15, 0])
  # screen.blit(baler, baler_rect)
  return baler_rect
  #rotate lines to right

def moveleft(baler_rect):
  #move baler right
  baler_rect= baler_rect.move([15, 0])
  return baler_rect
  # screen.blit(baler, baler_rect)

def moveup(tractor_rect, track_rect):
  #move baler right
  tractor_rect= tractor_rect.move([0, -5])
  track_rect= track_rect.move([0, -5])

  return tractor_rect, track_rect

def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

error= 5


pygame.init()

size= width, height = 600, 600
white= 255, 255, 255
speed= [0, -1]
baler_speed= [0, 0]

screen= pygame.display.set_mode(size)

tractor= pygame.image.load("tractor.png")
tractor_rect= tractor.get_rect()
tractor_rect.y= height- tractor_rect.height
tractor_rect.x= (width/2)- (tractor_rect.width/2)

baler= pygame.image.load("baler.png")
baler_rect= baler.get_rect()
baler_rect.y= 0
baler_rect.x= (width/2)- (baler_rect.width/2)

track= pygame.image.load("track.png")
track_rect= track.get_rect()
track_rect.y= height - track_rect.height*.5 - tractor_rect.height
track_rect.x= (width/2)- (track_rect.width/2)
trackAngle = 0
i= 0

while(1):
    DIST_LEFT = distance(TRIG_LEFT, ECHO_LEFT)
    DIST_RIGHT = distance(TRIG_RIGHT, ECHO_RIGHT)

    if abs(DIST_LEFT - DIST_RIGHT) <= error:
        print "move forward"
    elif DIST_LEFT <= DIST_RIGHT + error:
        print "turn left"
    else:
        print "turn right"