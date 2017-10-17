import sys, pygame

def moveright(baler_rect):
  #move baler left
  baler_rect= baler_rect.move([-2, 0])
  # screen.blit(baler, baler_rect)
  print "moving"
  return baler_rect
  #rotate lines to right

def moveleft(baler_rect):
  #move baler right
  baler_rect= baler_rect.move([2, 0])
  # screen.blit(baler, baler_rect)
  print "also moving"
  #rotate lines to left

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
screen= pygame.display.set_mode(size)

tractor_speed= [0, -1]
baler_speed= [0, 0]

tractor= pygame.image.load("tractor.png")
tractor_rect= tractor.get_rect()
tractor_rect.y= height- tractor_rect.height
tractor_rect.x= (width/2)- (tractor_rect.width/2)

track= pygame.image.load("track.png")
track_rect= track.get_rect()
track_rect.y= height - track_rect.height*.5 - tractor_rect.height
track_rect.x= (width/2)- (track_rect.width/2)

baler= pygame.image.load("baler.png")
baler_rect= baler.get_rect()
baler_rect.y= 0
baler_rect.x= (width/2)- (baler_rect.width/2)

i= 0
while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()

  tractor_rect= tractor_rect.move(tractor_speed)
  # baler_rect= moveleft(baler_rect)
  baler_rect= baler_rect.move(baler_speed)
  track_rect= track_rect.move(tractor_speed)
  track1= rot_center(track, -i)
  screen.fill(white)
  screen.blit(tractor, tractor_rect)
  screen.blit(baler, baler_rect)
  screen.blit(track1, track_rect)
  pygame.display.flip()
  i=i+1




