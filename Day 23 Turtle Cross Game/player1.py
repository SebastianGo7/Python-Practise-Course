from turtle import Turtle
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.shape("turtle")
        self.left(90)
        self.setposition(0, -270)

    def up(self):
        self.forward(MOVE_DISTANCE)
