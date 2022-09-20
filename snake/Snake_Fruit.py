import pygame


# Class for moving snake
class fruit:

    def __init__(self,x,y):
        self.x=x
        self.y=y



    # Method mooving entity
    def move(self,x,y):
        self.x = x
        self.y = y

    # Method getting x
    def getX(self):
        return (self.x)

    # Method getting y
    def getY(self):
        return (self.y)

    # Method set x et y
    def setXY(self,x,y):
        self.x=x
        self.y=y


    # Method getting picture
    def getIMG(self):
        return self.image

