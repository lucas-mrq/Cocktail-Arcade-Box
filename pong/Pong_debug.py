from Pong import Pong_Game


scorePong=[1,0]
pong = Pong_Game(scorePong)
scorePong[:]=pong.game()

print(scorePong)