import pygame
import random
import time
from snake.Snake_Snake import snake
from snake.Snake_Fruit import fruit
import os
import RPi.GPIO as GPIO


class Snake_Game:

    def __init__(self):
    
        # Intialisation of pygame
        pygame.init()

        # Create Screen
        self.screen_x = 1000
        self.screen_y = 600
        self.screen_y_adapt=768
        self.screen = pygame.display.set_mode((self.screen_x,self.screen_y_adapt),pygame.FULLSCREEN) # L'écran fait 1024*600

        # Background
        self.background = pygame.image.load('snake/img/fond.png')

        # Title and Icon
        pygame.display.set_caption("Snake")

        # FPS (frames per second) controller
        self.fps = pygame.time.Clock()
        
        # defining colors
        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.blue = pygame.Color(0, 0, 255)

        # Snake
        self.longueur_snake= 6
        self.snake_position = [100,50]

        # un rectangle va faire 30 de long et 30 de large
        self.snake_body = [snake(self.snake_position[0]-rect*30, self.snake_position[1]) for rect in range(self.longueur_snake)]

        self.direction = 'DOWN'
        self.change_to = self.direction

        # initial score
        self.score = 0

        # Initialise fruit
        self.pomme = pygame.image.load('snake/img/pomme.png')
        self.pomme_pos = fruit(random.randrange(1, ((self.screen_x-30)//10)) * 10,random.randrange(1, ((self.screen_y-30)//10)) * 10)
        self.fruit_appear = True

        # Définistions interruptions
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        self.run = True


    # Closing window if the user stop
    def stillRunning(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                pygame.quit()

    # Closing window if the user lose
    def game_over(self):

        font_over = pygame.font.SysFont("comicsansms", 100)
        text_over = font_over.render("Game over", True, (0,0,0))
        text_over1 = pygame.transform.rotate(text_over, -90)
        self.screen.blit(text_over1,(550,120))

        self.show_score((420,220),50)

        #font_replay = pygame.font.SysFont("comicsansms", 40)
        #text_replay = font_replay.render("Press right to play again", True, (0,0,0))
        #screen.blit(text_replay,(280,330))
        #pygame.draw.rect(screen,(0,0,0),(160,80,680,400),3)

        pygame.draw.rect(self.screen,(0,0,0),(320,40,320,520),3)
        pygame.display.update()
        time.sleep(5)

        pygame.quit()

    # displaying Score function
    def show_score(self,pos,taille):

        # creating font object score_font
        font = pygame.font.SysFont("comicsansms", taille)

        # create the display surface object
        text = font.render('Score : ' + str(self.score), True, (0,0,0))
        text1 = pygame.transform.rotate(text, -90)
        

        # displaying text
        self.screen.blit(text1,pos)

    def game(self):

        while self.run:

            # Joystick
            if (GPIO.input(1)==False):
                self.direction = 'LEFT'
                
            if (GPIO.input(7)==False):
                self.direction = 'RIGHT'
                
            if (GPIO.input(8)==False):
                self.direction = 'DOWN'

            if (GPIO.input(11)==False):
                self.direction = 'UP'

            # Moving the snake
            if self.direction == 'UP':
                self.snake_position[1] -= 15
            if self.direction == 'DOWN':
                self.snake_position[1] += 15
            if self.direction == 'LEFT':
                self.snake_position[0] -= 15
            if self.direction == 'RIGHT':
                self.snake_position[0] += 15

            # If the snake eat a fruit or not
            self.snake_body.insert(0,snake(self.snake_position[0],self.snake_position[1]))
            if self.pomme_pos.getX()-15<self.snake_position[0] and self.snake_position[0]<self.pomme_pos.getX()+15 and self.pomme_pos.getY()-15<self.snake_position[1] and self.snake_position[1]<self.pomme_pos.getY()+15:
                self.fruit_appear = False
                self.score+=10
            else:
                self.snake_body.pop()

            if not self.fruit_appear:  # on change la position de la pomme si elle a été touchée
                self.pomme_pos.setXY(random.randrange(1, ((self.screen_x-30)//10)) * 10, random.randrange(1, ((self.screen_y-30)//10)) * 10)

            self.fruit_appear = True

            # Draw the element in the map
            for rect in range(len(self.snake_body)):
                pygame.draw.rect(self.screen, self.green,pygame.Rect(self.snake_body[rect].getX(),self.snake_body[rect].getY(), 30, 30))

            # Draw eyes
            if self.direction == 'UP' or self.direction == 'DOWN':
                pygame.draw.circle(self.screen, self.black, (self.snake_body[0].getX()+20,self.snake_body[0].getY()+15), 3) #2.5 à l'origine
                pygame.draw.circle(self.screen, self.black, (self.snake_body[0].getX()+10,self.snake_body[0].getY()+15), 3)

            if self.direction == 'RIGHT' or self.direction == 'LEFT':
                pygame.draw.circle(self.screen, self.black, (self.snake_body[0].getX()+15,self.snake_body[0].getY()+20), 3)
                pygame.draw.circle(self.screen, self.black, (self.snake_body[0].getX()+15,self.snake_body[0].getY()+10), 3)

            self.show_score((970,10),30)
            pygame.display.update()

            # Game over conditions
            # Touching tje limits of the map
            if self.snake_position[0] < 0 or self.snake_position[0] > self.screen_x-35:
                self.game_over()
            if self.snake_position[1] < 5 or self.snake_position[1] > self.screen_y-35:
                self.game_over()

            #Touching itself
            for rect in range(1,len(self.snake_body)):
                if self.snake_position[0] == self.snake_body[rect].getX() and self.snake_position[1] == self.snake_body[rect].getY():
                    self.game_over()
                    return 0

            self.stillRunning()
            self.screen.blit(self.background,(0,0))
            self.screen.blit(self.pomme,(self.pomme_pos.getX(),self.pomme_pos.getY()))
            self.fps.tick(10)
