	# #define trigPin1 3
	# #define echoPin1 2
	# #define trigPin2 4
	# #define echoPin2 5
	# #define error 1

	# long duration, RightSensor, LeftSensor;

	# void setup()
	# {
 #  	Serial.begin (9600);
 #  	pinMode(trigPin1, OUTPUT);
 #  	pinMode(echoPin1, INPUT);
 #  	pinMode(trigPin2, OUTPUT);
 #  	pinMode(echoPin2, INPUT);
	# }

	# void loop()
	# {
 #  	SonarSensor(trigPin1, echoPin1, LeftSensor);
 #  	// LeftSensor = distancel;
 #  	SonarSensor(trigPin2, echoPin2, RightSensor);
 #  	// RightSensor = distancer;

 # 	//if(LeftSensor == RightSensor)
	# //if(LeftSensor < (RightSensor + error) && LeftSensor > (RightSensor - error))
	# if( Math.abs(RightSensor - LeftSensor) < error)
 #  	{
 #   	Serial.println("move forward");
	# // Show graphic for moveForwardArrow
 #  	}
	# else if( LeftSensor > RightSensor) 
 # 	//else if(LeftSensor > RightSensor)
 #  	{
 #    	Serial.println("turn right");
 #  	}
 # 	else
 #  	{
 #     	Serial.println("turn left");
 #  	}
 #  	Serial.print(LeftSensor);
 #  	Serial.print("   ");
 #  	Serial.println(RightSensor);

 #  	delay(500);
	# }

	# void SonarSensor(int trigPin,int echoPin, distance)
	# {
 #  	digitalWrite(trigPin, LOW);
 #  	delayMicroseconds(2);
 #  	digitalWrite(trigPin, HIGH);
 #  	delayMicroseconds(10);
 #  	digitalWrite(trigPin, LOW);
 #  	duration = pulseIn(echoPin, HIGH);
 #  	distance = (duration/2) / 29.1;
	# }

import sys, pygame

def moveright(baler_rect):
  #move baler left
  baler_rect= baler_rect.move([-2, 0])
  # screen.blit(baler, baler_rect)
  return baler_rect
  #rotate lines to right

def moveleft(baler_rect):
  #move baler right
  baler_rect= baler_rect.move([2, 0])
  return baler_rect
  # screen.blit(baler, baler_rect)

def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

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
while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()

  #tractor_rect= tractor_rect.move(speed)
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_LEFT:
      print('left')
      baler_rect= moveleft(baler_rect)
      trackAngle = trackAngle + 10
    elif event.key == pygame.K_RIGHT:
      print('right')
      baler_rect= moveright(baler_rect)
      trackAngle = trackAngle - 10
  baler_rect= baler_rect.move(baler_speed)
  #track_rect= track_rect.move(speed)
  track1= rot_center(track, trackAngle) #rotates 
  screen.fill(white)
  screen.blit(tractor, tractor_rect)
  screen.blit(baler, baler_rect)
  screen.blit(track1, track_rect)
  pygame.display.flip()
  i=i+1




