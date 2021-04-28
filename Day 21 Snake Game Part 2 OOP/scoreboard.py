from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 22, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.setposition(0, 265)
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Scoreboard: {self.score}", align=ALIGNMENT, font=FONT)

    def refresh_score(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
