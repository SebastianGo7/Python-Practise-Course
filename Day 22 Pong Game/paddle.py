from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.setposition(position)

    def up(self):
        actual_ycor = self.ycor()
        actual_xcor = self.xcor()
        self.setposition(actual_xcor, actual_ycor + 20)

    def down(self):
        actual_ycor = self.ycor()
        actual_xcor = self.xcor()
        self.setposition(actual_xcor, actual_ycor - 20)
