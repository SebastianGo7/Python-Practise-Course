from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.direction = "up"

    def random_start(self):
        self.setposition(0, 0)
        random_angle = random.randint(0, 70)
        self.setheading(random_angle)
        self.forward(2)

    def move(self):
        self.forward(10)

    def bounce_walls(self):
        actual_heading = self.heading()
        extra_angle = (360 - (actual_heading*2))
        self.right(-extra_angle)

    def bounce_paddle(self):
        actual_heading = self.heading()
        extra_angle = 180 + (2*actual_heading)
        self.right(extra_angle)
