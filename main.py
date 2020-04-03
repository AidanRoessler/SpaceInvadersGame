import pygame
import time 
import sys


pygame.init()
clock = pygame.time.Clock()
width=800
height=600
screen=pygame.display.set_mode((800,600))


ship=pygame.image.load("spaceship.png")
shipRect=ship.get_rect()
#Set inital postion of rect at center of the screen
shipRect.centerx = (width//2)
shipRect.centery = (height//2)
screen.blit(ship,shipRect)

blast=pygame.image.load("energyball.png")
blastRect=blast.get_rect()
blastRect.centerx=(shipRect.centerx)
blastRect.centery=((shipRect.centery) + 20 )
blastSpeed=[10,10]


while True:
  screen.fill((255,100,200))
  clock.tick(30)
  keyInput=pygame.key.get_pressed()
  if keyInput[pygame.K_ESCAPE]:
    pygame.quit()
    sys.exit()
  for e in pygame.event.get():
    if e.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  if keyInput[pygame.K_LEFT]:
   shipRect.centerx -= 2
  if keyInput[pygame.K_RIGHT]:
   shipRect.centerx += 2
  if keyInput[pygame.K_UP]:
     screen.blit(blast,blastRect)
     blastRect.centery -= 1
     screen.blit(blast,blastRect)
     pygame.display.flip()
  screen.blit(ship,shipRect)
  pygame.display.flip()
 