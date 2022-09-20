import pygame
import keyboard
from pong.Pong_Player import player
from pong.Pong_Ball import ball
import time
import os
import RPi.GPIO as GPIO

class Pong_Game:

    def __init__(self,tabScore):

        # defining colors
        self.WHITE = (255, 255, 255)
        self.black = (0,0,0)
        
        self.encore=1

        # Intialisation of pygame
        pygame.init()

        # Create Screen
        self.screen_x = 1024
        self.screen_y = 600
        self.screen_y_adapt=768
        self.screen = pygame.display.set_mode((self.screen_x,self.screen_y_adapt),pygame.FULLSCREEN) # L'écran fait 1024*600

        # Title and Icon
        pygame.display.set_caption("Pong")

        # FPS (frames per second) controller
        self.fps = pygame.time.Clock()

        self.totalScore=tabScore

        self.score_player1=0
        self.score_player2=0
        self.taille_raquette = 85
        self.acceleration=1
        self.player1=player(0,5)
        self.player2=player(self.screen_x-15,self.screen_y-5-self.taille_raquette)
        self.ball=ball(512,300,2,1,13)

        # Définistions interruptions
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        self.run = True

    def game_over(self):
        time.sleep(7)
        pygame.quit()
        self.encore=0

    # displaying Score function
    def show_final_score(self,score_player1, score_player2):

        # creating font object score_font
        font = pygame.font.SysFont("comicsansms", 45)
        font_result = pygame.font.SysFont("comicsansms", 80)
        font_score = pygame.font.SysFont("comicsansms",30)

        # create the display surface object
        text1 = font_score.render('Score : ' + str(score_player1), True, self.WHITE)
        text2 = font_score.render('Score : ' + str(score_player2), True, self.WHITE)
        text_over = font.render("Round over", True, self.WHITE)
        victory = font_result.render('+1 point', True, self.WHITE)
        defeat = font_result.render('Oups...', True, self.WHITE)

        text_over1 = pygame.transform.rotate(text_over, -90)
        text_over2 = pygame.transform.rotate(text_over, 90)
        text1 = pygame.transform.rotate(text1, -90)
        text2 = pygame.transform.rotate(text2, 90)


        self.screen.fill((self.black))
        for rect in range(0,12):
            pygame.draw.rect(self.screen,self.WHITE,(int(self.screen_x/2)-2,rect*50,4,45))  # barres au milieu

        # displaying text
        self.screen.blit(text_over1,(450,15))
        self.screen.blit(text_over2,(540,430))
        self.screen.blit(text1,(10,480))
        self.screen.blit(text2,(980,15))
        if score_player1 >score_player2:
            victory = pygame.transform.rotate(victory, -90)
            defeat = pygame.transform.rotate(defeat, 90)
            self.screen.blit(victory,(250,210))
            self.screen.blit(defeat,(720,230))

        else:
            victory = pygame.transform.rotate(victory, 90)
            defeat = pygame.transform.rotate(defeat, -90)
            self.screen.blit(victory,(720,190))
            self.screen.blit(defeat,(230,190))


        pygame.display.update()


    def game(self):

        while self.run:

            # Key event
            if (GPIO.input(13)==False):
                if (self.player2.getY()>0):
                    self.player2.setY(self.player2.getY()-3)
            if (GPIO.input(6)==False):
                if (self.player2.getY()<self.screen_y-self.taille_raquette):
                    self.player2.setY(self.player2.getY()+3)

            if (GPIO.input(11)==False):
                if (self.player1.getY()>0):
                    self.player1.setY(self.player1.getY()-3)
            if (GPIO.input(8)==False):
                if (self.player1.getY()<self.screen_y-self.taille_raquette):
                    self.player1.setY(self.player1.getY()+3)


            if self.encore!=0:
                self.screen.fill((self.black))

            # Rebond à droite et gauche
            if (self.ball.getX()>self.screen_x-self.ball.getRayon()) or (self.ball.getX()<self.ball.getRayon()):
                self.ball.setdx(-self.ball.getdx())
                if (self.ball.getX()>self.screen_x-self.ball.getRayon()):
                    self.score_player1+=1
                else:
                    self.score_player2+=1

            # Rebond en haut et en bas
            if ((self.ball.getY()<self.ball.getRayon()) or (self.ball.getY()>self.screen_y-self.ball.getRayon())):
                self.ball.setdy(-self.ball.getdy())

            # Rebond sur la raquette du joueur gauche
            if ((self.player1.getX()+11<self.ball.getX()-self.ball.getRayon()<self.player1.getX()+17)):   # si compris dans le bon x
                if(self.player1.getY()-self.ball.getRayon()<self.ball.getY()<self.player1.getY()+self.taille_raquette+self.ball.getRayon()): #si dans la raquette entière
                    if(self.player1.getY()+15<self.ball.getY()<self.player1.getY()+self.taille_raquette-15):# si seulement dans la partie centrale de la raquette
                        self.ball.setdx(-self.ball.getdx())

                    else:
                        if self.ball.getdx()<0: self.ball.setdx((-(self.ball.getdx())+self.acceleration))
                        else: self.ball.setdx((-(self.ball.getdx())-self.acceleration))
                        if self.ball.getdy()<0: self.ball.setdy((-(self.ball.getdy())+self.acceleration))
                        else: self.ball.setdy((-(self.ball.getdy())-self.acceleration))

            # Rebond sur la raquette du joueur droit
            if (self.player2.getX()-2<self.ball.getX()+self.ball.getRayon()<self.player2.getX()+5):
                if(self.player2.getY()-self.ball.getRayon()<self.ball.getY()<self.player2.getY()+self.taille_raquette+self.ball.getRayon()): #si dans la raquette entière
                    if(self.player2.getY()+15<self.ball.getY()<self.player2.getY()+self.taille_raquette-15):# si seulement dans la partie centrale de la raquette
                        self.ball.setdx(-self.ball.getdx())

                    else:
                        if self.ball.getdx()<0: self.ball.setdx((-(self.ball.getdx())+self.acceleration))
                        else: self.ball.setdx((-(self.ball.getdx())-self.acceleration))
                        if self.ball.getdy()<0: self.ball.setdy(-((self.ball.getdy())+self.acceleration))
                        else: self.ball.setdy(-((self.ball.getdy())-self.acceleration))

            self.ball.move(self.ball.getX()+self.ball.getdx(),self.ball.getY()+self.ball.getdy())

            for rect in range(0,12):
                pygame.draw.rect(self.screen,self.WHITE,(int(self.screen_x/2)-2,rect*50,4,45))  #barres au milieu
            pygame.draw.rect(self.screen, self.WHITE, (self.player1.getX(),self.player1.getY(),15,85))  # affichage player1
            pygame.draw.rect(self.screen, self.WHITE, (self.player2.getX(),self.player2.getY(),15,85))  # affichage player2
            pygame.draw.circle(self.screen, self.WHITE, (int(self.ball.getX()),int(self.ball.getY())),self.ball.getRayon())  # affichae balle

            pygame.display.update()

            if (self.score_player1==1) or (self.score_player2==1):
                time.sleep(1)
                self.show_final_score(self.score_player1+self.totalScore[0],self.score_player2+self.totalScore[1])
                self.game_over()
                return [self.score_player1+self.totalScore[0],self.score_player2+self.totalScore[1]]

            self.fps.tick(80)

