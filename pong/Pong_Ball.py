# Class for moving ball
class ball:

    def __init__(self,x,y,dx,dy,rayon):
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy
        self.rayon=rayon



    # Method mooving entity
    def move(self,x,y):
        self.x = x
        self.y = y

    # Method to set dx
    def setdx(self,dx):
        self.dx=dx

    # Method to set dy
    def setdy(self,dy):
        self.dy=dy


    # Method getting x
    def getX(self):
        return (self.x)

    # Method getting dx
    def getdx(self):
        return (self.dx)

    # Method getting y
    def getY(self):
        return (self.y)

    # Method getting dy
    def getdy(self):
        return (self.dy)

    # Method getting rayon
    def getRayon(self):
        return (self.rayon)



