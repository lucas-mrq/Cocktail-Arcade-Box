import pygame
import keyboard



# Class for moving player
class player:

    def __init__(self,x,y):
        self.x=x
        self.y=y



    # Method mooving entity
    def setY(self,y):
        self.y = y

    # Method getting x
    def getX(self):
        return (self.x)

    # Method getting y
    def getY(self):
        return (self.y)

