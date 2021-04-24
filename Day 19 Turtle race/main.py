from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Choose your favourite"
                                                          "red, green, blue, yellow, black, orange, brown")

color_array = ["red", "green", "blue", "yellow", "black", "orange", "brown"]
all_turtles = []
for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color_array[i])
    new_turtle.goto(x=-225, y=(-100 + 40 * i))
    all_turtles.append(new_turtle)

is_race_on = False
if user_bet:
    is_race_on = True

winner = ""

while is_race_on:
    i = 0
    for turtle in all_turtles:

        rand_distance = random.randint(0, 20)
        turtle.forward(rand_distance)

        if turtle.pos()[0] > 230:
            winner = color_array[i]
            is_race_on = False

        i += 1


if user_bet == winner:
    print(f"The {winner} won. Congratulations, you chose the right turtle")
else:
    print(f"The {winner} won. Sorry, you bet on the wrong turtle")

screen.exitonclick()


# Other functions to practise
#
# def move_forwards():
#     Anna.forward(10)
#
# def move_backwards():
#     Anna.backward(10)
#
# def move_clockwise():
#     Anna.right(20)
#
# def move_counter_clockwise():
#     Anna.left(20)
#
# def move_clear_drawing():
#     Anna.setpos(0,0)
#     Anna.clear()
#
# screen.listen()
# screen.onkey(key ="w",fun= move_forwards)
# screen.onkey(key ="s",fun= move_backwards)
# screen.onkey(key ="a",fun= move_clockwise)
# screen.onkey(key ="d",fun= move_counter_clockwise)
# screen.onkey(key ="c",fun= move_clear_drawing)
#
