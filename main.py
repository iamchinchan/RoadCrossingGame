from turtle import Screen
from scoreboard import Scoreboard
from carManager import CarManager
from player import Player
import time

screen  = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)


player = Player()
scoreboard = Scoreboard()
carManager = CarManager()
screen.listen()
screen.onkeypress(key="Up",fun=player.move)

isGameOn=True
while isGameOn:
  screen.update()
  # create a new car
  carManager.createNewCar(scoreboard.level)
  
  # check if its a collision
  if carManager.checkCollision(player.position()):
    # true if it is a collision
    print("game over")
    player.died()
    scoreboard.gameOver()
    screen.update()
    isGameOn=False
    # wait for 0.1 second and move all cars and then it will update cars again in  next loop

  # check if player reached the deadline
  if player.onDestination():
    # print("reached destionation")
    # change level
    # screen.clear()
    scoreboard.increaseLevel()
    player.resetPlayer()
    carManager.increaseSpeed()
    # carManager.deletePreviousLevelCars()
    
    
  time.sleep(.1)
  # print("player position is: ",player.position())
  carManager.moveCars()
screen.exitonclick()