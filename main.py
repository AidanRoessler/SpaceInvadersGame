import pygame
import time 
import sys
import random

alienPositions={"alienOne":[1000,2000,False],"alienTwo":[1000,2000,False],"alienThree":[1000,2000,False]}
score=0
count=0
pygame.init()
pygame.font.init()
myFont = pygame.font.SysFont('Comic Sans MS', 46)
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

def alienSetup(alienName,x,y):
  
  #Ensuring that the hit aliens are off the screen
  if alienPositions[str(alienName)][2]:
    alienPositions[str(alienName)]=[1000,2000,True]
    return(False)#Had to put the return here to get out of the function 
  if count==0:
    alienPositions[str(alienName)]=[x,y,False] #Had to put this at the top b/c pygames changes the name of the surface once the image is loaded in
   alienName=pygame.image.load("alien.png")
   alienNameRect=alienName.get_rect()
   alienNameRect.centerx=x
   alienNameRect.centery=y
  if count>0:
   alienName=pygame.image.load("alien.png")
   alienNameRect=alienName.get_rect()
   moveX=random.randint(-2,2)
   moveY=random.randint(-2,2)
  #Reverse direction if it is near/below the space ship 
   alienNameRect.centerx += moveX
   alienNameRect.centery += moveY
 

def setupAllAliens():
  alienSetup("alienOne",100,200)
  alienSetup("alienTwo",300,200)
  alienSetup("alienThree",500,200)

def scoreUpdater():
  score=0
  for k in (alienPositions.keys()):
    if alienPositions[k][2]:
      score+=1
  scoreSurface=myFont.render("Score: "+str(score),True,(0,0,0))
  screen.blit(scoreSurface,(280,100))

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
   print("Inital centery" + str(blastRect.centery))
   blastRect.centerx=(shipRect.centerx)
   blastRect.centery=((shipRect.centery) + 20 )
   while blastRect.centery >0:
     blastRect.centery -= 1
     screen.blit(blast,blastRect)
     setupAllAliens()
     pygame.display.flip()
     for i in (alienPositions.keys()):
       print(alienPositions[i][1])
       if (((blastRect.centery)-(alienPositions[i][1])<=50) and ((blastRect.centerx)-(alienPositions[i][0])<=50)):
         print(str(i)+ " hit")
         #Moves aliens off the screen if they are hit
         alienPositions[str(i)]=[1000,2000,True]
                
  screen.blit(ship,shipRect)
  setupAllAliens()
  scoreUpdater()
  pygame.display.flip()
 