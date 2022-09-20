import pygame
from pacman.PacMan_Class import entity,player
from PIL import Image
import numpy as np 
import random
import time
import os
import RPi.GPIO as GPIO

class PacMan_Game:

    def __init__(self):

        self.PACMAN_SIZE = 27
        self.gameOver=pygame.image.load("pacman/img/gameOver1.png")
        
        # Définistions interruptions
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(0, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)

                # Intialisation of pygame
        pygame.init()

        # Create Screen
        self.screen = pygame.display.set_mode((1024,768),pygame.FULLSCREEN)

        # Background
        self.background = pygame.image.load('pacman/img/emptyMap.png')

        # Title and Icon
        pygame.display.set_caption("PacMan")

        # Player
        self.player = [player('pacman',"player",k) for k in range(2)]
        self.mobs = [entity('img/mob'+str(k+1)+'.png',"mob") for k in range(3)]
        self.petitsRond = [entity('img/rondP.png',"petitRond") for k in range(194)]
        self.grandsRond = [entity('img/rondG.png',"grandRond") for k in range(4)]
        self.fruit = entity('img/fraise.png',"fraise")

        self.invincibility=[0,0]

        for i in range(len(self.mobs)):
            self.mobs[i].move(410+75*i,290)

        self.startMobs=[-1,0,-1]
        self.run = True

        self.a=1
        self.score=0

        self.comptRouge=0
        self.comptJaune=0
        
        self.police = pygame.font.Font(None,72)
        self.tabScore=[self.police.render("Score 0",True,pygame.Color("#FFFF00")),self.police.render("Score 1",True,pygame.Color("#FFFF00"))]


        #Chargement de la map
        self.im = Image.open('img/emptyMapRail.png').convert('RGB') 
        self.na = np.array(self.im) 
        self.high=self.na.shape[0]
        self.length=self.na.shape[1]
        self.posFruit=[]

        self.run=True
        self.a=0

        for i in range(self.high):

            loadingText=self.police.render("Chargement",True,pygame.Color("#FFFF00"))

            chargement=int(((i+1)*100)/self.high)
            if chargement<10:
                chargement="0"+str(chargement)+" %"
            else:
                chargement=str(chargement)+" %"

            loading=self.police.render(chargement,True,pygame.Color("#FFFF00"))
            self.screen.blit(self.background,(0,0))
            self.screen.blit(loading,[480,290]) #&&
            self.screen.blit(loadingText,[370,190]) #&&
            pygame.display.update()


            for j in range(self.length):
                if(self.na[i,j][0]==255 and self.na[i,j][1]==242 and self.na[i,j][2]==0):
                    self.grandsRond[self.comptJaune].move(j-5,i-5)
                    self.comptJaune+=1
                if(self.na[i,j][0]==237 and self.na[i,j][1]==28 and self.na[i,j][2]==36):
                    self.posFruit.append([j-22,i-20])
                    self.petitsRond[self.comptRouge].move(j-3,i-3)
                    self.comptRouge+=1

        self.player[0].move(450-self.PACMAN_SIZE,418-self.PACMAN_SIZE)
        self.player[1].move(570-self.PACMAN_SIZE,418-self.PACMAN_SIZE)
        self.player[1].dir=3

        self.secondsStart = int(time.time())
        self.startFruit=0
        self.fruit.pos=[-50,-50]

        self.police = pygame.font.Font(None,48) #**

        self.tabScore=[[self.police.render("J1",True,pygame.Color("#FFFF00")),[450,10]],[self.police.render("J2",True,pygame.Color("#FFFF00")),[550,10]],[self.police.render(str(self.player[0].getScore()),True,pygame.Color("#FFFF00")),[400,10]],[self.police.render(str(self.player[1].getScore()),True,pygame.Color("#FFFF00")),[600,10]]]
        self.tabScore[0][0]=pygame.transform.rotate(self.tabScore[0][0], 270)
        self.tabScore[1][0]=pygame.transform.rotate(self.tabScore[1][0], 90)
        self.tabScore[2][0]=pygame.transform.rotate(self.tabScore[2][0], 270)
        self.tabScore[3][0]=pygame.transform.rotate(self.tabScore[3][0], 90)
        

    def collision(self, monster, player,joueur=1):

        if joueur!=1:
            posMonster=monster.getIMG(0).get_rect()
        else:
            posMonster=monster.getIMG().get_rect()

        posPlayer=player.getIMG(0).get_rect()
    	#if ((posMonster[0]+dimMonster[0]/2>posPlayer[0] and posMonster[0]+dimMonster[0]/2<posPlayer[0]+PACMAN_SIZE and posMonster[1]>posPlayer[1] and posMonster[1]<posPlayer[1]+PACMAN_SIZE) or (posMonster[0]+dimMonster[0]>posPlayer[0] and posMonster[0]+dimMonster[0]<posPlayer[0]+PACMAN_SIZE and posMonster[1]+dimMonster[1]/2>posPlayer[1] and posMonster[1]+dimMonster[1]/2<posPlayer[1]+PACMAN_SIZE) or (posMonster[0]+dimMonster[0]/2>posPlayer[0] and posMonster[0]+dimMonster[0]/2<posPlayer[0]+PACMAN_SIZE and posMonster[1]+dimMonster[1]>posPlayer[1] and posMonster[1]+dimMonster[1]<posPlayer[1]+PACMAN_SIZE) or (posMonster[0]>posPlayer[0] and posMonster[0]<posPlayer[0]+PACMAN_SIZE and posMonster[1]+dimMonster[1]/2>posPlayer[1] and posMonster[1]+dimMonster[1]/2<posPlayer[1]+PACMAN_SIZE)):
    	#	return True
    	#else:
    	#	return False

        posMonster.x+=monster.getPos()[0]
        posMonster.y+=monster.getPos()[1]
        posPlayer.x+=player.getPos()[0]
        posPlayer.y+=player.getPos()[1]

        if posMonster.colliderect(posPlayer)== 1:
            return True
        else:
            return False

        # Function to display players
    def playerDisplay(self,petitsRond,start,gameOver,invincibilit):
        self.run=True
        self.player[0].nextPos(self.PACMAN_SIZE,self.na)
        self.player[1].nextPos(self.PACMAN_SIZE,self.na)

        for i in range(3):
            if start[i]==1:
                self.mobs[i].nextChoice(self.PACMAN_SIZE,self.na)
                self.mobs[i].nextChoice(self.PACMAN_SIZE,self.na)

        listIndex=[]
        for i in range(len(petitsRond)-1):
            if petitsRond[i].aval(self.PACMAN_SIZE,self.player[0].getPos()):
                listIndex.append(i)
                self.player[0].addPoint(1)
            elif petitsRond[i].aval(self.PACMAN_SIZE,self.player[1].getPos()):
                listIndex.append(i)
                self.player[1].addPoint(1)
            else:
                self.screen.blit(petitsRond[i].getIMG(),petitsRond[i].getPos())

        for enti in self.grandsRond:
            if enti.aval(self.PACMAN_SIZE,self.player[0].getPos()):
                enti.move(-5,-5)
                self.player[0].addPoint(10)
                invincibilit[0]=1
            elif enti.aval(self.PACMAN_SIZE,self.player[1].getPos()):
                enti.move(-5,-5)
                self.player[1].addPoint(10)
                print(self.player[1].getScore())
                invincibilit[1]=1
            else:
                if enti.getPos()[0]>-1:
                    self.screen.blit(enti.getIMG(),enti.getPos())

        for i in range(3):
            if self.collision(self.mobs[i],self.player[0]):
    #           print("collision mob",str(i)+"-joueur0")
                if invincibilit[0]==0:
                    self.run=False
                else:
                    self.player[0].score+=10
                    start[i]=100
                    self.mobs[i].move(486,290)


            if self.collision(self.mobs[i],self.player[1]):
                #print("collision mob",str(i)+"-joueur1")
                if invincibilit[1]==0:
                    gameOver=pygame.image.load("pacman/img/gameOver2.png")
                    self.run=False
                else:
                    self.player[1].score+=10
                    start[i]=100
                    self.mobs[i].move(486,290)

        if self.collision(self.player[1],self.player[0],2):
                if (invincibilit[1]==0 and invincibilit[0]>1) or (invincibilit[0]==invincibilit[1] and self.player[0].getScore()>self.player[1].getScore()):
                    gameOver=pygame.image.load("pacman/img/gameOver2.png")
                    self.run=False
                elif (invincibilit[1]>1 and invincibilit[0]==0) or (invincibilit[0]==invincibilit[1] and self.player[0].getScore()<self.player[1].getScore()):
                    self.run=False

        for i in range(2):
            if self.collision(self.fruit,self.player[i]):
                #print("self.collision fruit")
                invincibilit[i]=1
                self.fruit.move(1000,1000)              

        L2=petitsRond[:]
        petitsRond=[]
        for j in range(len(L2)):
            if j not in listIndex:
                petitsRond.append(L2[j])

        for i in range(2):
            if invincibilit[i]>0:
                invincibilit[i]+=1
                if invincibilit[i]==200:
                    invincibilit[i]=0
                else:
                    self.screen.blit(self.player[i].getIMG(4),self.player[i].getPos())
            else:
                self.screen.blit(self.player[i].getIMG(0),self.player[i].getPos())

        for enti in self.mobs+[self.fruit]:
            self.screen.blit(enti.getIMG(),enti.getPos())


        self.tabScore[2][0]=self.police.render(str(self.player[0].getScore()), True, pygame.Color("white"))
        self.tabScore[3][0]=self.police.render(str(self.player[1].getScore()), True, pygame.Color("white"))

        self.tabScore[2][0]=pygame.transform.rotate(self.tabScore[2][0], 270)
        self.tabScore[3][0]=pygame.transform.rotate(self.tabScore[3][0], 90)


        for scor in self.tabScore:
            self.screen.blit(scor[0],scor[1])

        return petitsRond.copy(),self.run,gameOver


    def game(self):

        while self.run:
            if (GPIO.input(26)==False):
                self.player[1].next=[1, 0]
            elif (GPIO.input(13)==False):
                self.player[1].next=[0, -1]
            elif (GPIO.input(19)==False):
                self.player[1].next=[-1, 0]
            elif (GPIO.input(6)==False):
                self.player[1].next=[0, 1]
            if (GPIO.input(7)==False):
                self.player[0].next=[1, 0]
            elif (GPIO.input(11)==False):
                self.player[0].next=[0, -1]
            elif (GPIO.input(1)==False):
                self.player[0].next=[-1, 0]
            elif (GPIO.input(8)==False):
                self.player[0].next=[0, 1]

            if (int(time.time())-self.secondsStart)%10==0 and (int(time.time())-self.secondsStart)!=0:
                if self.startFruit==0:
                    self.startFruit=1
                    self.fruit.pos=random.choice(self.posFruit)
            else:
                self.startFruit=0

            #print(self.mobs[0].getPos())

            for i in range(len(self.startMobs)):
                if self.startMobs[i]>10:
                    self.startMobs[i]-=1
                if self.startMobs[i]==0 or self.startMobs[i]==10:
                    if self.mobs[i].getPos()[1]!=189:
                        self.mobs[i].move(self.mobs[i].getPos()[0],self.mobs[i].getPos()[1]-1)
                    else:
                        self.startMobs[i]=1
                        self.mobs[i].now=[random.choice([-1,1]),0]

                elif self.startMobs[i]==2:
                    if self.mobs[i].getPos()[0]!=486:
                        self.mobs[i].move(self.mobs[i].getPos()[0]+1,self.mobs[i].getPos()[1])
                    else:
                        self.startMobs[i]=0

                elif self.startMobs[i]==3:
                    if self.mobs[i].getPos()[0]!=486:
                        self.mobs[i].move(self.mobs[i].getPos()[0]-1,self.mobs[i].getPos()[1])
                    else:
                        self.startMobs[i]=0

            if self.player[0].getScore()+self.player[1].getScore()>=20 and self.player[0].getScore()+self.player[1].getScore()<=29 and self.startMobs[0]==-1:
                self.startMobs[0]=2

            if self.player[0].getScore()+self.player[1].getScore()>=40 and self.player[0].getScore()+self.player[1].getScore()<=49 and self.startMobs[2]==-1:
                self.startMobs[2]=3
            
            # Backgroung Image
            self.screen.blit(self.background,(0,0))
            self.petitsRond2,self.run,self.gameOver=self.playerDisplay(self.petitsRond,self.startMobs,self.gameOver,self.invincibility)
            self.petitsRond=self.petitsRond2.copy()
            pygame.display.update()


    def end(self):

        self.run=True

        while self.run:
    
            self.a+=1
            
            if self.a>500:
                self.run=False
            if (GPIO.input(5)==False):
                self.run=False
            if (GPIO.input(0)==False):
                self.run=False
            
            
            
            self.screen.blit(self.gameOver,(0,0))

            for enti in self.mobs+[self.fruit]:
                self.screen.blit(enti.getIMG(),enti.getPos())

            for enti in self.player:
                self.screen.blit(enti.getIMG(0),enti.getPos())

            pygame.display.update()
        pygame.quit()