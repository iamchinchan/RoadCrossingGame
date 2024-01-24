FONT=  ("Courier",24,"normal")
from turtle import Turtle
class Scoreboard(Turtle):
  def __init__(self)->None:
    super().__init__()
    self.level=1
    self.penup()
    self.hideturtle()
    self.goto((-280, 265))
    self.updateScore()
    
  def updateScore(self):
    self.clear()
    self.write(f"Level: {self.level}",align="left",font=FONT)
  
  def increaseLevel(self):
    self.level+=1
    self.updateScore()
    
  def gameOver(self):
    self.goto((0,0))
    self.write("Game Over",align="center",font=FONT)