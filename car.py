from turtle import Turtle
from random import choice , randint
COLORS=["red","orange","yellow","green","blue","purple"]
class Car(Turtle):
  def __init__(self)->None:
    super().__init__()
    # self.moveDistance = moveDistance
    self.speed("fastest")
    self.shape("square")
    self.shapesize(stretch_len=2, stretch_wid=1) #20*40
    self.setheading(180)
    self.color(choice(COLORS))
    self.penup()
    self.goto((randint(320,330),randint(-250,250)))
    
  def move(self,moveDistance):
    self.forward(moveDistance)