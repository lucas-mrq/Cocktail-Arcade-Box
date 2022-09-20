import pygame
import time
import os
import RPi.GPIO as GPIO
from pong.Pong import Pong_Game


class Pong_Menu:

    def __init__(self):

        self.scorePong=[0,0]
        self.nbr_points=1
        self.white = (255, 255, 255)
        self.black = (0,0,0)
        self.fps = pygame.time.Clock()
        self.run = True

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(1,GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(7,GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(0,GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(5,GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # Intialisation of pygame
        pygame.init()

        # Create Screen
        self.screen_x=1024
        self.screen_y=600
        self.screen_y_adapt=768
        self.screen = pygame.display.set_mode((self.screen_x,self.screen_y_adapt),pygame.FULLSCREEN)

        # Title and Icon
        pygame.display.set_caption("Menu Pong")

        #Background
        self.background = pygame.image.load('pong/img/image_menu.png')

        self.font_score= pygame.font.SysFont("comicsansms", 45)


    def selection(self):
        pause = 0
        while self.run:

            if (GPIO.input(7)==False):
                self.nbr_points+=1
                pause=1
            if (GPIO.input(1)==False):
                if (self.nbr_points>1):
                    self.nbr_points-=1
                pause=1
            if (GPIO.input(0)==False):
                while self.scorePong[0] != self.nbr_points and self.nbr_points!=self.scorePong[1]:
                    pong = Pong_Game(self.scorePong)
                    self.scorePong[:]=pong.game()
                pygame.quit()
                return(0)
            if (GPIO.input(5)==False):
                pygame.quit()
                return(0)


            self.screen.blit(self.background,(0,0))
            self.text_score = self.font_score.render(str(self.nbr_points), True, self.white)
            self.text_score1 = pygame.transform.rotate(self.text_score, -90)
            self.screen.blit(self.text_score1,(320,290))
            self.fps.tick(50)
            pygame.display.update()

            if (pause==1):
                time.sleep(0.5)
                pause = 0

        pygame.quit()

    def end(self):

        white = (255, 255, 255)
        black = (0,0,0)

        # Intialisation of pygame
        pygame.init()

        # Create Screen
        screen_x = 1024
        screen_y = 600
        screen_y_adapt=768
        screen = pygame.display.set_mode((screen_x,screen_y_adapt),pygame.FULLSCREEN) # L'écran fait 1024*600

        # Title and Icon
        pygame.display.set_caption("Game over Pong")

        # creating font object score_font
        font = pygame.font.SysFont("comicsansms", 45)
        font_result = pygame.font.SysFont("comicsansms", 80)
        font_score = pygame.font.SysFont("comicsansms",30)

        # create the display surface object
        text1 = font_score.render('Score : ' + str(self.scorePong[0]), True, white)
        text2 = font_score.render('Score : ' + str(self.scorePong[1]), True, white)
        text_over = font.render("Game over", True, white)
        victory = font_result.render('Victory !', True, white)
        defeat = font_result.render('Defeat ...', True, white)

        text_over1 = pygame.transform.rotate(text_over, -90)
        text_over2 = pygame.transform.rotate(text_over, 90)
        text1 = pygame.transform.rotate(text1, -90)
        text2 = pygame.transform.rotate(text2, 90)

        if self.scorePong[0] >self.scorePong[1]:
            victory = pygame.transform.rotate(victory, -90)
            defeat = pygame.transform.rotate(defeat, 90)
        else:
            victory = pygame.transform.rotate(victory, 90)
            defeat = pygame.transform.rotate(defeat, -90)

        
        for rect in range(0,12):
            pygame.draw.rect(screen,white,(screen_x/2-2,rect*50,4,45))  # barres au milieu



        # displaying text
        screen.blit(text_over1,(450,15))
        screen.blit(text_over2,(540,430))
        screen.blit(text1,(10,480))
        screen.blit(text2,(980,15))

        if self.scorePong[0] >self.scorePong[1]:
            screen.blit(victory,(250,210))
            screen.blit(defeat,(720,210))

        else:
            screen.blit(victory,(720,170))
            screen.blit(defeat,(230,170))

        pygame.display.update()
    
        time.sleep(5)
        pygame.quit()








