from menu.Menu import Menu_Game
from pacman.PacMan import PacMan_Game
from snake.Snake import Snake_Game
from pong.Pong_Menu import Pong_Menu
import time

jeu = "menu"

while jeu!="end":

	jeu = "menu"

	while jeu=="menu":
		menu=Menu_Game()
		jeu=menu.selection()

	if jeu=="pacman":	
		pacman = PacMan_Game()
		pacman.game()
		pacman.end()

	elif jeu=="pong":
		time.sleep(1)
		menu_pong = Pong_Menu()
		wait=menu_pong.selection()
		menu_pong.end() 

	elif jeu=="snake":
		snake = Snake_Game()
		wait=snake.game()
		