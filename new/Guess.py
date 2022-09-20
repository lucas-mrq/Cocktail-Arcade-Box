import pygame
import os
import RPi.GPIO as GPIO
import time
import random



# Définistions interruptions
GPIO.setmode(GPIO.BCM)
GPIO.setup(1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(0, GPIO.IN, pull_up_down=GPIO.PUD_UP)



class Guess_Game:

    def __init__(self):
        # defining colors
        self.white = (255, 255, 255)
        self.black = (0,0,0)

        # Intialisation of pygame
        pygame.init()

        # Create Screen
        self.screen_x = 1024
        self.screen_y = 600
        self.screen_y_adapt=768
        self.screen = pygame.display.set_mode((self.screen_x,self.screen_y_adapt),pygame.FULLSCREEN) # L'écran fait 1024*600

        # Title and Icon
        pygame.display.set_caption("Guess the number")

        # FPS (frames per second) controller
        self.fps = pygame.time.Clock()

        self.font_choose = pygame.font.SysFont("comicsansms", 36)
        self.choose1 = self.font_choose.render('Nombre entre 1 et 100:', True, self.white)
        self.choose = pygame.transform.rotate(self.choose1, -90)

        self.font_number = pygame.font.SysFont("comicsansms", 82)

        self.font_over=pygame.font.SysFont("comicsansms",86)
        self.over1 = self.font_over.render('Victory !', True, self.white)
        self.over = pygame.transform.rotate(self.over1, -90)

        self.font_defeat=pygame.font.SysFont("comicsansms",86)
        self.defeat1 = self.font_over.render('Defeat ...', True, self.white)
        self.defeat = pygame.transform.rotate(self.defeat1, -90)

        self.font_tour=pygame.font.SysFont("comicsansms",30)

        self.font_help=pygame.font.SysFont("comicsansms",56)



    def check(self, number_choose, number_to_guess,tour_restant):
        if number_choose>number_to_guess and tour_restant>=0:
            return('grand')
        elif number_choose<number_to_guess and tour_restant>=0:
            return('petit')
        else:
            return('ok')




    def game(self):
        time.sleep(1)
        run=True
        res='nul'
        number_to_guess=random.randint(1,100)
        number_selected = 'X'
        number_choose=1
        tour_restant=6

        while run:
            self.screen.fill((self.black))

            if (GPIO.input(7)==False and number_choose<100):
                number_choose+=1
                time.sleep(0.3)
            if (GPIO.input(1)==False and number_choose>1):
                number_choose-=1
                time.sleep(0.3)
            if (GPIO.input(8)==False and number_choose<91):
                number_choose+=10
                time.sleep(0.3)
            if (GPIO.input(11)==False and number_choose>10):
                number_choose-=10
                time.sleep(0.3)
            if (GPIO.input(0)==False):
                time.sleep(0.3)
                tour_restant-=1
                res = self.check(number_choose,number_to_guess,tour_restant)
                number_selected=number_choose




            self.screen.blit(self.choose,(600,100))
            self.number1 = self.font_number.render(str(number_choose), True, self.white)
            self.number = pygame.transform.rotate(self.number1, -90)
            self.screen.blit(self.number,(300,250))

            self.grand1 = self.font_help.render(str(number_selected) +': Trop grand !', True, self.white)
            self.petit1 = self.font_help.render(str(number_selected) +': Trop petit !', True, self.white)
            self.grand = pygame.transform.rotate(self.grand1, -90)
            self.petit = pygame.transform.rotate(self.petit1, -90)




            if res == 'grand':
                self.screen.blit(self.grand,(20,120))
            elif res == 'petit':
                self.screen.blit(self.petit,(20,120))
            elif res =='ok':
                self.screen.fill((self.black))
                self.screen.blit(self.over,(470,140))
                pygame.display.update()
                run=False

            if tour_restant==0 and res!='ok':
                self.screen.fill((self.black))
                self.screen.blit(self.defeat,(470,140))
                pygame.display.update()
                run=False

            self.tour1 = self.font_tour.render('Tour restant: '+ str(tour_restant), True, self.white)
            self.tour = pygame.transform.rotate(self.tour1, -90)
            self.screen.blit(self.tour,(980,20))


            pygame.display.update()
        time.sleep(4)
        pygame.quit()


