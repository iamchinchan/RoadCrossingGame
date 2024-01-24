from car import Car
from random import randint
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT=5


class CarManager():
  def __init__(self)->None:
    self.cars=[]
    self.carSpeed= STARTING_MOVE_DISTANCE
  def createNewCar(self,level):
    random_chance = randint(1,6)
    if random_chance ==1:
      newCar = Car()
      self.cars.append(newCar)
    
  def moveCars(self):
    # print(f"moving cars, total cars to move: ",len(self.cars))
    for car in self.cars:
      if car.xcor()<-330:
        # car is gone out of screen and destroy that car
        # print(f"removing a car from car manager, ars now: ",len(self.cars))
        self.cars.remove(car)
        car.hideturtle()
        del car
        # print(f"cares left on screen : {len(self.cars)}")
        # pass
      else:
        car.move(self.carSpeed)
    # print(f"moved cars, total cars which was moved: ",len(self.cars))
      
  def checkCollision(self,position)->bool:
    isCollision = False
    playerYPosition = position[1]
    # print(f"player y position is: ",playerYPosition)
    for car in self.cars:
      if car.xcor()<=30 and car.xcor()>-30:
        # check if also collides on y axis
        if car.ycor()<playerYPosition+25 and car.ycor()>playerYPosition-20:
          # its a collision
          isCollision=True
          break
    return isCollision

  def increaseSpeed(self):
    self.carSpeed+=MOVE_INCREMENT
  # def deletePreviousLevelCars(self):
  #   while len(self.cars):
  #     self.cars[0].hideturtle()
  #     car  = self.cars.pop()
  #     del car