from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()

winner = Turtle()
winner.setposition(0, 225)
winner.penup()
winner.hideturtle()
winner.color("white")
score_right = 0
score_left = 0


screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")

# l and a might seem strange however they are right
# next to each other in the Neo Layout.
screen.onkey(paddle2.up, "l")
screen.onkey(paddle2.down, "a")

game_is_on = True
while game_is_on:
    screen.update()
    ball.random_start()
    point_is_on = True

    while point_is_on:
        time.sleep(0.05)
        screen.update()
        ball.move()

        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_walls()

        if ball.xcor() > 330:
            if 50 > ball.ycor()-paddle1.ycor() > -50 or 50 > ball.ycor()+paddle1.ycor() > -50:
                ball.bounce_paddle()

        if ball.xcor() < -330:
            if 50 > ball.ycor()-paddle2.ycor() > -50 or 50 > ball.ycor()+paddle2.ycor() > -50:
                ball.bounce_paddle()

        if ball.xcor() > 370:
            winner.clear()
            score_left += 1
            winner.clear()
            winner.write(f"Score: Left:{score_left} Right: {score_right}", align="center", font=("Arial", 30, "normal"))
            point_is_on = False

        if ball.xcor() < -370:
            score_right += 1
            winner.clear()
            winner.write(f"Score: Left:{score_left} Right: {score_right}", align="center", font=("Arial", 30, "normal"))
            point_is_on = False

    if score_left == 5:
        winner.clear()
        winner.write(f"Left Wins, final score: Left{score_left} Right {score_right}", align="center",
                     font=("Arial", 30, "normal"))
        game_is_on = False

    elif score_right == 5:
        winner.clear()
        winner.write(f"Right Wins, final score: Left{score_left} Right {score_right}", align="center",
                     font=("Arial", 30, "normal"))
        game_is_on = False


screen.exitonclick()
