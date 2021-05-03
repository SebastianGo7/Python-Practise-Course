from turtle import Turtle
from random import randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 7


class CarManager:
    def __init__(self):
        self.car_array = []
        self.speed = 0

    def create_car(self):
        car = Turtle()
        car.shape("square")
        car.color(COLORS[randint(0, 5)])
        car.penup()
        car.left(180)
        car.shapesize(1, 2)
        rand_y_position = randint(-250, 250)
        car.setposition(250, rand_y_position)
        car.forward(STARTING_MOVE_DISTANCE)
        self.car_array.append(car)

    def move(self, factor):
        for car in self.car_array:
            self.speed = STARTING_MOVE_DISTANCE + MOVE_INCREMENT*factor
            car.forward(self.speed)
