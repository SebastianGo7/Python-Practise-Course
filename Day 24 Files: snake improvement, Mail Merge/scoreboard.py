from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.high_score}", align=ALIGNMENT, font=FONT)



    def reset(self):
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        with open("data.txt") as file:
            highest_score = int(file.read())
        print(f"increase Score 1:   highscore:{highest_score}  selfscore:{self.score}")

        if self.score == highest_score:
            with open("data.txt", mode="w") as file:
                new_highest_score = highest_score + 1
                score_string = str(new_highest_score)
                file.write(score_string)
            print(f"increase Score 2:   highscore:{score_string} same as {highest_score}  selfscore:{self.score}")
            self.high_score = new_highest_score

        self.score += 1
        print(f"increase Score 3:   highscore:{highest_score}  selfscore:{self.score}")
        self.update_scoreboard()


