
import colorgram
from turtle import Turtle, Screen, colormode
import random



def extract_colors():
    # used to extract colors from dot painting, then copied return tuple into color_found_list
    colors = colorgram.extract('dots_hirst.jpg', 30)
    colors_list = []

    for i in range(10):
        entry = colors[i].rgb[0:]
        colors_list.append(entry)


#Task is to create a dot art using the turtle module


art_turtle = Turtle()

art_turtle.hideturtle()
art_turtle.width(4)
art_turtle.speed
art_turtle.penup()

color_found_list = [(133, 164, 201),(223, 151, 102),(30, 43, 63),(201, 136, 147),(160, 61, 50),(235, 212, 88)]

colormode(255)
random_color = random.randint(0,len(color_found_list)-1)

art_turtle.backward(225)
art_turtle.right(90)
art_turtle.forward(225)
art_turtle.left(90)

for n in range (15):
    for i in range (15):
        art_turtle.forward(30)
        art_turtle.dot(20, random.choice(color_found_list))
    art_turtle.backward(450)
    art_turtle.left(90)
    art_turtle.forward(30)
    art_turtle.right(90)


screen = Screen()
screen.exitonclick()