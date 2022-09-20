import pygame
import os
import RPi.GPIO as GPIO
import pygame
import os
import time


class Menu_Game:

	def __init__(self):

		self.newGame=0
		self.newArchive="menu,pacman,pong,snake,Launcher.py,addNewGame.py"
		
		GPIO.setmode(GPIO.BCM)
		 
		GPIO.setup(5,GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(0,GPIO.IN, pull_up_down=GPIO.PUD_UP)

		GPIO.setup(1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)		 

		# Intialisation of pygame
		pygame.init()

		# Create Screen
		self.screen = pygame.display.set_mode((1024,768),pygame.FULLSCREEN)

		# Title and Icon
		pygame.display.set_caption("Menu")

		# Background
		self.background = pygame.image.load('menu/img/background.png')

		self.start=""

		self.selectMenu=0

		self.menu=[pygame.image.load("menu/img/menu1.png"),pygame.image.load("menu/img/menu2.png")]
		self.pacman=pygame.image.load("menu/img/pacman.png")
		self.snake=pygame.image.load("menu/img/snake.png")
		self.pong=pygame.image.load("menu/img/pong.png")
		self.futur1=pygame.image.load("menu/img/futur1.png")
		self.futur2=pygame.image.load("menu/img/futur2.png")
		self.futur3=pygame.image.load("menu/img/futur3.png")
		self.futur4=pygame.image.load("menu/img/futur4.png")
		self.futur5=pygame.image.load("menu/img/futur5.png")
		self.valid=pygame.image.load("menu/img/valid.png")
		self.cancel=pygame.image.load("menu/img/cancel.png")

		self.run = True
		self.up,self.down,self.right,self.left,self.a,self.b=False,False,False,False,False,False

		# Initialisation
		self.posPacMan=[530,128]
		self.posSnake=[2000,2000]
		self.posPong=[2000,2000]
		self.posFutur1=[2000,2000]
		self.posFutur2=[2000,2000]
		self.posFutur3=[2000,2000]
		self.posFutur4=[2000,2000]
		self.posFutur5=[2000,2000]


	def selection(self):

		tour=True

		while self.run:

			if self.selectMenu==0:

				while tour!=True:
					if (GPIO.input(5)==False):
						pygame.quit()
						return "end"
						tour=True
					if (GPIO.input(0)==False):
						self.a=True
						tour=True
					if (GPIO.input(8)==False):
						self.right=True
						tour=True
					if (GPIO.input(7)==False):
						self.up=True
						tour=True
					if (GPIO.input(11)==False):
						self.left=True
						tour=True
					if (GPIO.input(1)==False):
						self.down=True
						tour=True
					
				tour=False
				if self.posPacMan[0]<2000:
					if self.a:
						self.start="PacMan"
						self.run=False
					elif self.right:
						self.posPacMan=[2000,2000]
						self.posSnake=[530,356]
						self.right=False

					elif self.down:
						self.posPacMan=[2000,2000]
						self.posPong=[345,128]
						self.down=False
					else:
						self.left=False
						self.up=False

				elif self.posSnake[0]<2000:
					if self.a:
						self.start="Snake"
						self.run=False
					elif self.left:
						self.posSnake=[2000,2000]
						self.posPacMan=[530,128]
						self.left=False
					elif self.right:
						self.posSnake=[2000,2000]
						self.posPacMan=[2000,2000]
						self.posFutur2=[530,128]
						self.right=False
						self.selectMenu=1
					elif self.down:
						self.posSnake=[2000,2000]
						self.posFutur1=[345,358]
						self.down=False
					else:
						self.up=False

				elif self.posFutur1[0]<2000:
					if self.a:
						self.start="Futur1"
						self.run=False
					elif self.left:
						self.posFutur1=[2000,2000]
						self.posPong=[345,128]
						self.left=False
					elif self.up:
						self.posFutur1=[2000,2000]
						self.posSnake=[530,356]
						self.up=False
					elif self.right:
						self.posFutur4=[345,128]
						self.posFutur1=[2000,2000]
						self.right=False
						self.selectMenu=1
					else:
						self.down=False

				elif self.posPong[0]<2000:
					if self.a:
						self.start="Pong"
						self.run=False
					if self.right:			
						self.posPong=[2000,2000]
						self.posFutur1=[345,358]
						self.right=False
					elif self.up:
						self.posPong=[2000,2000]
						self.posPacMan=[530,128]
						self.up=False
					else:
						self.left=False
						self.down=False

				self.screen.blit(self.background,(0,0))
				self.screen.blit(self.menu[self.selectMenu],(250,13))
				self.screen.blit(self.pacman,self.posPacMan)
				self.screen.blit(self.snake,self.posSnake)
				self.screen.blit(self.pong,self.posPong)
				self.screen.blit(self.futur1,self.posFutur1)
				self.screen.blit(self.futur2,self.posFutur2)
				self.screen.blit(self.futur3,self.posFutur3)
				self.screen.blit(self.futur4,self.posFutur4)
				self.screen.blit(self.futur5,self.posFutur5)
				pygame.display.update()
				time.sleep(0.2)

			elif self.selectMenu==1:

				while tour!=True:
					if (GPIO.input(5)==False):     
						pygame.quit()
						return "end"
						tour=True
					if (GPIO.input(0)==False):
						self.a=True
						tour=True
					if (GPIO.input(8)==False):
						self.right=True
						tour=True
					if (GPIO.input(7)==False):
						self.up=True
						tour=True
					if (GPIO.input(11)==False):
						self.left=True
						tour=True
					if (GPIO.input(1)==False):
						self.down=True
						tour=True
						
				tour=False

				if self.posFutur2[0]<2000:
					if self.a:
						self.start="Futur2"
						self.run=False
					elif self.right:
						self.posFutur2=[2000,2000]
						self.posFutur3=[530,356]
						self.right=False
					elif self.down:
						self.posFutur2=[2000,2000]
						self.posFutur4=[345,128]
						self.down=False
					elif self.left:
						self.posFutur2=[2000,2000]
						self.posSnake=[530,356]
						self.down=False
						self.selectMenu=0
					else:
						self.left=False
						self.up=False

				elif self.posFutur3[0]<2000:
					if self.a:
						self.start="Futur3"
						self.run=False
					elif self.left:
						self.posFutur3=[2000,2000]
						self.posFutur2=[530,128]
						self.left=False
					elif self.down:
						self.posFutur3=[2000,2000]
						self.posFutur5=[345,358]
						self.down=False
					else:
						self.up=False
						self.right=False

				elif self.posFutur5[0]<2000:
					if self.a:
						self.start="Futur5"
						self.run=False
					elif self.left:
						self.posFutur5=[2000,2000]
						self.posFutur4=[345,128]
						self.left=False
					elif self.up:
						self.posFutur5=[2000,2000]
						self.posFutur2=[530,356]
						self.up=False
					else:
						self.down=False
						self.right=False

				elif self.posFutur4[0]<2000:
					if self.a:
						self.start="Futur4"
						self.run=False
					if self.right:			
						self.posFutur4=[2000,2000]
						self.posFutur5=[345,358]
						self.right=False
					elif self.up:
						self.posFutur4=[2000,2000]
						self.posFutur2=[530,128]
						self.up=False
					elif self.left:
						self.posFutur4=[2000,2000]
						self.posFutur1=[345,358]
						self.selectMenu=0
						self.up=False
					else:
						self.down=False

				self.screen.blit(self.background,(0,0))
				self.screen.blit(self.menu[self.selectMenu],(250,13))
				self.screen.blit(self.pacman,self.posPacMan)
				self.screen.blit(self.snake,self.posSnake)
				self.screen.blit(self.pong,self.posPong)
				self.screen.blit(self.futur1,self.posFutur1)
				self.screen.blit(self.futur2,self.posFutur2)
				self.screen.blit(self.futur3,self.posFutur3)
				self.screen.blit(self.futur4,self.posFutur4)
				self.screen.blit(self.futur5,self.posFutur5)
				pygame.display.update()
				time.sleep(0.2)


			if self.start=="PacMan":
				pacmanRun=True
				self.screen.blit(self.background,(0,0))
				self.screen.blit(self.menu[0],(250,13))
				self.screen.blit(self.pacman,self.posPacMan)
				self.screen.blit(self.snake,self.posSnake)
				self.screen.blit(self.pong,self.posPong)
				self.screen.blit(self.futur1,self.posFutur1)
				self.screen.blit(self.cancel,(100,197))
				self.screen.blit(self.valid,(100,315))
				pygame.display.update()
				time.sleep(0.2)
				while pacmanRun:
					if (GPIO.input(5)==False):
						return "menu"
					elif (GPIO.input(0)==False):
						return "pacman"
					else:
						self.screen.blit(self.background,(0,0))
						self.screen.blit(self.menu[0],(250,13))
						self.screen.blit(self.pacman,self.posPacMan)
						self.screen.blit(self.snake,self.posSnake)
						self.screen.blit(self.pong,self.posPong)
						self.screen.blit(self.futur1,self.posFutur1)
						self.screen.blit(self.cancel,(100,197))
						self.screen.blit(self.valid,(100,315))
						pygame.display.update()


			if self.start=="Snake":
				snakeRun=True
				time.sleep(0.2)
				while snakeRun:
					if (GPIO.input(5)==False):
						return "menu"
					elif (GPIO.input(0)==False):
						return "snake"
					else:
						self.screen.blit(self.background,(0,0))
						self.screen.blit(self.menu[0],(250,13))
						self.screen.blit(self.pacman,self.posPacMan)
						self.screen.blit(self.snake,self.posSnake)
						self.screen.blit(self.pong,self.posPong)
						self.screen.blit(self.futur1,self.posFutur1)
						self.screen.blit(self.cancel,(100,197))
						self.screen.blit(self.valid,(100,315))
						pygame.display.update()
						
			if self.start=="Pong":
				pongRun=True
				self.screen.blit(self.background,(0,0))
				self.screen.blit(self.menu[0],(250,13))
				self.screen.blit(self.pacman,self.posPacMan)
				self.screen.blit(self.snake,self.posSnake)
				self.screen.blit(self.pong,self.posPong)
				self.screen.blit(self.futur1,self.posFutur1)
				self.screen.blit(self.cancel,(100,197))
				self.screen.blit(self.valid,(100,315))
				pygame.display.update()
				time.sleep(0.2)
				while pongRun:
					if (GPIO.input(5)==False):
						return "menu"
					elif (GPIO.input(0)==False):
						return "pong"
					else:
						self.screen.blit(self.background,(0,0))
						self.screen.blit(self.menu[0],(250,13))
						self.screen.blit(self.pacman,self.posPacMan)
						self.screen.blit(self.snake,self.posSnake)
						self.screen.blit(self.pong,self.posPong)
						self.screen.blit(self.futur1,self.posFutur1)
						self.screen.blit(self.cancel,(100,197))
						self.screen.blit(self.valid,(100,315))
						pygame.display.update()
						
			if self.start=="Futur1":
				futur1Run=True
				self.screen.blit(self.background,(0,0))
				self.screen.blit(self.menu[0],(250,13))
				self.screen.blit(self.pacman,self.posPacMan)
				self.screen.blit(self.snake,self.posSnake)
				self.screen.blit(self.pong,self.posPong)
				self.screen.blit(self.futur1,self.posFutur1)
				self.screen.blit(self.cancel,(100,197))
				self.screen.blit(self.valid,(100,315))
				pygame.display.update()
				time.sleep(0.2)
				while futur1Run:
					if (GPIO.input(5)==False):
						return "menu"
					elif (GPIO.input(0)==False):
						return "futur1"
					else:
						self.screen.blit(self.background,(0,0))
						self.screen.blit(self.menu[0],(250,13))
						self.screen.blit(self.pacman,self.posPacMan)
						self.screen.blit(self.snake,self.posSnake)
						self.screen.blit(self.pong,self.posPong)
						self.screen.blit(self.futur1,self.posFutur1)
						self.screen.blit(self.cancel,(100,197))
						self.screen.blit(self.valid,(100,315))
						pygame.display.update()

			if self.start=="Futur2":
				futur2Run=True
				self.screen.blit(self.background,(0,0))
				self.screen.blit(self.menu[1],(250,13))
				self.screen.blit(self.futur2,self.posFutur2)
				self.screen.blit(self.futur3,self.posFutur3)
				self.screen.blit(self.futur4,self.posFutur4)
				self.screen.blit(self.futur5,self.posFutur5)
				self.screen.blit(self.cancel,(100,197))
				self.screen.blit(self.valid,(100,315))
				pygame.display.update()
				time.sleep(0.2)
				while futur2Run:
					if (GPIO.input(5)==False):
						return "menu"
					elif (GPIO.input(0)==False):
						return "futur2"
					else:
						self.screen.blit(self.background,(0,0))
						self.screen.blit(self.menu[1],(250,13))
						self.screen.blit(self.futur2,self.posFutur2)
						self.screen.blit(self.futur3,self.posFutur3)
						self.screen.blit(self.futur4,self.posFutur4)
						self.screen.blit(self.futur5,self.posFutur5)
						self.screen.blit(self.cancel,(100,197))
						self.screen.blit(self.valid,(100,315))
						pygame.display.update()

			if self.start=="Futur3":
				futur3Run=True
				self.screen.blit(self.background,(0,0))
				self.screen.blit(self.menu[1],(250,13))
				self.screen.blit(self.futur2,self.posFutur2)
				self.screen.blit(self.futur3,self.posFutur3)
				self.screen.blit(self.futur4,self.posFutur4)
				self.screen.blit(self.futur5,self.posFutur5)
				self.screen.blit(self.cancel,(100,197))
				self.screen.blit(self.valid,(100,315))
				pygame.display.update()
				time.sleep(0.2)
				while futur3Run:
					if (GPIO.input(5)==False):
						return "menu"
					elif (GPIO.input(0)==False):
						return "futur3"
					else:
						self.screen.blit(self.background,(0,0))
						self.screen.blit(self.menu[1],(250,13))
						self.screen.blit(self.futur2,self.posFutur2)
						self.screen.blit(self.futur3,self.posFutur3)
						self.screen.blit(self.futur4,self.posFutur4)
						self.screen.blit(self.futur5,self.posFutur5)
						self.screen.blit(self.cancel,(100,197))
						self.screen.blit(self.valid,(100,315))
						pygame.display.update()

			if self.start=="Futur4":
				futur4Run=True
				self.screen.blit(self.background,(0,0))
				self.screen.blit(self.menu[1],(250,13))
				self.screen.blit(self.futur2,self.posFutur2)
				self.screen.blit(self.futur3,self.posFutur3)
				self.screen.blit(self.futur4,self.posFutur4)
				self.screen.blit(self.futur5,self.posFutur5)
				self.screen.blit(self.cancel,(100,197))
				self.screen.blit(self.valid,(100,315))
				pygame.display.update()
				time.sleep(0.2)
				while futur4Run:
					if (GPIO.input(5)==False):
						return "menu"
					elif (GPIO.input(0)==False):
						return "futur4"
					else:
						self.screen.blit(self.background,(0,0))
						self.screen.blit(self.menu[1],(250,13))
						self.screen.blit(self.futur2,self.posFutur2)
						self.screen.blit(self.futur3,self.posFutur3)
						self.screen.blit(self.futur4,self.posFutur4)
						self.screen.blit(self.futur5,self.posFutur5)
						self.screen.blit(self.cancel,(100,197))
						self.screen.blit(self.valid,(100,315))
						pygame.display.update()

			if self.start=="Futur5":
				futur5Run=True
				self.screen.blit(self.background,(0,0))
				self.screen.blit(self.menu[1],(250,13))
				self.screen.blit(self.futur2,self.posFutur2)
				self.screen.blit(self.futur3,self.posFutur3)
				self.screen.blit(self.futur4,self.posFutur4)
				self.screen.blit(self.futur5,self.posFutur5)
				self.screen.blit(self.cancel,(100,197))
				self.screen.blit(self.valid,(100,315))
				pygame.display.update()
				time.sleep(0.2)
				while futur5Run:
					if (GPIO.input(5)==False):
						return "menu"
					elif (GPIO.input(0)==False):
						return "futur5"
					else:
						self.screen.blit(self.background,(0,0))
						self.screen.blit(self.menu[1],(250,13))
						self.screen.blit(self.futur2,self.posFutur2)
						self.screen.blit(self.futur3,self.posFutur3)
						self.screen.blit(self.futur4,self.posFutur4)
						self.screen.blit(self.futur5,self.posFutur5)
						self.screen.blit(self.cancel,(100,197))
						self.screen.blit(self.valid,(100,315))
						pygame.display.update()