import pygame
import time 
import sys
import random

alienPositions=[[1000,2000,False,0],[1000,2000,False,0],[1000,2000,False,0]]
score=0
count=0
energyBallFlag=False
rightEnd=False
leftEnd=False
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

def alienSetup(alienName,x,y,index):
  global leftEnd
  global rightEnd
  #Ensuring that the hit aliens are off the screen
  if alienPositions[index][2]:
    alienPositions[index]=[1000,3000,True,0]
    return(False)#Had to put the return here to get out of the function 
  alienName=pygame.image.load("alien.png")
  alienNameRect=alienName.get_rect()
  if ((alienPositions[index][0]==1000) and (alienPositions[index][1]==2000)):
   alienNameRect.centerx=x
   alienNameRect.centery=y
   alienPositions[index][0]=alienNameRect.centerx
   alienPositions[index][1]=alienNameRect.centery
   return("Setup completed")#Had to put the return here to get out of the function 
  moveX=random.randint(0,10)
  moveY=random.randint(0,0)
  #Reverse direction if at the edge of the screen
  if ((alienPositions[index][0] >= 750)):
    alienPositions[index][3]=random.randint(500,1000)
    rightEnd=True
    leftEnd=False
  if ((alienPositions[index][0] <= 50)):
    alienPositions[index][3]=random.randint(500,1000)
    leftEnd=True
    rightEnd=False
  if ((alienPositions[index][3]>0) and (rightEnd)):
    moveX = -moveX
    alienPositions[index][3] -= 1
  if ((alienPositions[index][3]>0) and (leftEnd)):
    moveX = abs(moveX)
    alienPositions[index][3] -= 1
  if alienPositions[index][3]==1:
    leftEnd=False
    rightEnd=False
  if energyBallFlag:
    alienNameRect.centerx = alienPositions[index][0]
    alienNameRect.centery = alienPositions[index][1]
  else:
    alienNameRect.centerx = alienPositions[index][0] + moveX
    alienNameRect.centery = alienPositions[index][1] + moveY
  screen.blit(alienName,alienNameRect)
  pygame.display.flip()
  alienPositions[index][0]=alienNameRect.centerx
  alienPositions[index][1]=alienNameRect.centery
    
def setupAllAliens():
  alienSetup("alienOne",100,200,0)
  alienSetup("alienTwo",300,200,1)
  alienSetup("alienThree",500,200,2)

def scoreUpdater():
  score=0
  for k in range(len(alienPositions)):
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
   blastRect.centerx=(shipRect.centerx)
   blastRect.centery=((shipRect.centery) + 20 )
   while blastRect.centery >0:
     blastRect.centery -= 1
     screen.blit(blast,blastRect)
     energyBallFlag=True
     setupAllAliens()
     pygame.display.flip()
     for i in range(len(alienPositions)):
       if ((((blastRect.centery)-(alienPositions[i][1])<=50) and ((blastRect.centery)-(alienPositions[i][1])>=0)) and ((((blastRect.centerx)-(alienPositions[i][0])<=50) and ((blastRect.centerx)-(alienPositions[i][0])>=0)))):
         print("alien "+str(i+1)+ " hit")
         #Moves aliens off the screen if they are hit
         alienPositions[i]=[1000,3000,True]             
  screen.blit(ship,shipRect)
  energyBallFlag=False
  setupAllAliens()
  scoreUpdater()
  pygame.display.flip()
 