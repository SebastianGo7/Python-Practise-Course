from turtle import Turtle
import turtle
import pandas

# Game allows to guess states, it shows a map of the US, and the guessed states names can be seen on the card

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# This turtle is used to write the text
writerTurtle = Turtle()
writerTurtle.hideturtle()
writerTurtle.penup()
tracer = 0

states_names = pandas.read_csv("50_states.csv")
found_states_list = []
score = 0


game_is_on = True

while game_is_on:

    # continuous input of the user asking for states
    answer_state = (screen.textinput(title=f"Guess the state {score}/50", prompt="Can you guess another one?")).title()

    if answer_state == "Exit":
        break

    # First it is checked whether the state is within the names
    # Then the coordinates are taken and the writer turtle writes them on the screen
    for i in range(0, len(states_names.state)):

        if states_names.state[i] == answer_state:
            found_states_list.append(answer_state)
            x = states_names.x[i]
            y = states_names.y[i]
            writerTurtle.setposition(x, y)
            writerTurtle.write(f"{answer_state}", align="center", font=("arial", 15, "normal"))
            score += 1

    if score == 50:
        game_is_on = False
        writerTurtle.setposition(0, 270)
        writerTurtle.write(f"Congratulations, you won", align="center", font=("arial", 15, "normal"))

# saving the not guessed states in a csv file.
unknown_states = []
for state in states_names.state:
    if state not in found_states_list:
        unknown_states.append(state)

# Saving Data to a .csv file
data_for_csv = pandas.DataFrame(unknown_states)
data_for_csv.to_csv("states_to_study.csv")
