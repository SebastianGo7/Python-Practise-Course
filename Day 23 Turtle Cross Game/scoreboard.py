from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.hideturtle()
        self.penup()

    def write_level(self):
        self.setposition(-260, 250)
        self.write(f"Level {self.level}", align="left", font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write("Game Over", align="center", font=FONT)
