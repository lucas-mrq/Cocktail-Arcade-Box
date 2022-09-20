import pygame
import keyboard


# Class for moving snake
class snake:

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

    # Method getting direction
    def getDirection(self):
        return (self.direction)

    # Method set direction
    def setDirection(self,direction):
        self.direction=direction

