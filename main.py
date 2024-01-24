from turtle import Screen
from scoreboard import scoreboard
from carManager import CarManager
from player import Player
import time

screen  = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)



isGameOn=True
while isGameOn:
  time.sleep(.1)
  screen.update()
screen.exitonclick()