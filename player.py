from turtle import Turtle,Screen
STARTING_POSITION = (0,-280)
MOVE_DISTANCE =10 
FINISH_LINE_Y = 280

class Player(Turtle):
  def __init__(self)->None:
    # self.screen=screen
    super().__init__()
    self.shape("turtle")
    self.penup()
    self.setheading(90)
    # self.color("black")
    self.canMove=True
    self.resetPlayer()
    
  def resetPlayer(self):
    self.goto(STARTING_POSITION)
    # self.showturtle()
    
  def move(self):
    if self.canMove:
      self.forward(MOVE_DISTANCE)
    # self.screen.update()
    
  def onDestination(self):
    return self.ycor()>FINISH_LINE_Y
    
    
  def died(self):
    self.color("red")
    self.canMove=False