import pygame
import random

# Class for moving entity
class player:

    def __init__(self, img, nature,number):

        self.image=[]
        for i in range(4):
            imagetab=[]
            for j in range(6):
                imagetab.append(pygame.image.load("pacman/img/"+img+str(number*4+1+i)+"."+str(j)+".png"))
            self.image.append(imagetab)

        for i in range(4):
            imagetab=[]
            for j in range(6):
                imagetab.append(pygame.image.load("pacman/img/"+img+str(9+i)+"."+str(j)+".png"))
            self.image.append(imagetab)

        self.dir=1
        self.number=number
        self.mouv=0
        self.pos=[0,0]
        self.nature=nature
        self.next=[1,0]
        self.now=[0,-1]
        self.score=0

    # Method mooving entity
    def move(self,x,y):
        self.pos = [x,y]

    # Method getting position
    def getPos(self):
        return ([self.pos[0], self.pos[1]])

    # Method getting picture
    def getIMG(self,indice):
        self.mouv+=0.2
        return self.image[self.dir+indice][int(self.mouv%6)]

    # Method getting picture
    def setDIR(self,newpos):
        if newpos[0]<0:
            self.dir=2
        if newpos[0]>0:
            self.dir=0
        if newpos[1]<0:
            self.dir=3
        if newpos[1]>0:
            self.dir=1

    def getScore(self):
        return self.score

    def addPoint(self,point):
        self.score+=point

    def nextPos(self,PACMAN_SIZE, map):
        if (map[self.getPos()[1]+PACMAN_SIZE+2*self.next[1],self.getPos()[0]+PACMAN_SIZE+2*self.next[0]][0]!=0 or map[self.getPos()[1]+PACMAN_SIZE+2*self.next[1],self.getPos()[0]+PACMAN_SIZE+2*self.next[0]][1]!=0 or map[self.getPos()[1]+PACMAN_SIZE+2*self.next[1],self.getPos()[0]+PACMAN_SIZE+2*self.next[0]][2]!=0):
            self.move(self.getPos()[0]+2*self.next[0],self.getPos()[1]+2*self.next[1])
            if (self.now!=self.next):
                self.setDIR(self.next)
            self.now=self.next

        else:
            if( map[self.getPos()[1]+PACMAN_SIZE+2*self.now[1],self.getPos()[0]+PACMAN_SIZE+2*self.now[0]][0]!=0 or map[self.getPos()[1]+PACMAN_SIZE+2*self.now[1],self.getPos()[0]+PACMAN_SIZE+2*self.now[0]][1]!=0 or map[self.getPos()[1]+PACMAN_SIZE+2*self.now[1],self.getPos()[0]+PACMAN_SIZE+2*self.now[0]][2]!=0):
                self.move(self.getPos()[0]+2*self.now[0],self.getPos()[1]+2*self.now[1])
            else:
                self.now[0]=-self.next[0]
                self.now[1]=-self.next[1]
                self.dir=int((self.dir+2)%4)

class entity:

    def __init__(self, img, nature):

        self.image=pygame.image.load(img)
        self.direction=0
        self.pos=[0,0]
        self.posprev=[0,0]
        self.nature=nature
        self.now=[1,0]
        self.directions=[[1,0],[0,-1],[-1,0],[0,1]]

    # Method mooving entity
    def move(self,x,y):
        self.posprev=self.pos
        self.pos = [x,y]

    # Method getting position
    def getPos(self):
        return ([self.pos[0], self.pos[1]])

    # Method getting picture
    def getIMG(self):
        return self.image

    # Method getting picture
    def getNow(self):
        return self.now

    def nextChoice(self,PACMAN_SIZE,map):
        directions2=self.directions.copy()
        choice=[]
        for j in range(4):
            if (map[self.getPos()[1]+PACMAN_SIZE+directions2[j][1],self.getPos()[0]+PACMAN_SIZE+directions2[j][0]][0]!=0 or map[self.getPos()[1]+PACMAN_SIZE+directions2[j][1],self.getPos()[0]+PACMAN_SIZE+directions2[j][0]][1]!=0 or map[self.getPos()[1]+PACMAN_SIZE+directions2[j][1],self.getPos()[0]+PACMAN_SIZE+directions2[j][0]][2]!=0):
                choice.append(directions2[j])

        if len(choice)==2 and (choice[0][1]!=-choice[1][1] or choice[0][0]!=-choice[1][0]):
            positionNow=self.getNow()
            if choice[0][0]!=-positionNow[0] and choice[0][1]!=-positionNow[1] :
                self.now=choice[0]
            else:
                self.now=choice[1]

        if len(choice)>2:
            positionNow=self.getNow()
            tabPoss=[]
            for k in range(len(choice)):
                if choice[k][1]!=-positionNow[1] and choice[k][0]!=-positionNow[0]:
                    tabPoss.append(choice[k])

            self.now=random.choice(tabPoss)

        self.move(self.getPos()[0]+self.now[0],self.getPos()[1]+self.now[1])

    def aval(self,PACMAN_SIZE,joueur):
        return self.getPos()[0]<(joueur[0]+int(1.5*PACMAN_SIZE)) and  self.getPos()[0]>(joueur[0]+int(0.5*PACMAN_SIZE)) and self.getPos()[1]<(joueur[1]+int(1.5*PACMAN_SIZE)) and self.getPos()[1]>(joueur[1]+int(0.5*PACMAN_SIZE))