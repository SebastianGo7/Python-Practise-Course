import time
from turtle import Screen
from player1 import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

creating_cars_6th_cycle = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.clear()
    scoreboard.write_level()

    creating_cars_6th_cycle += 1
    if creating_cars_6th_cycle == 3:
        car_manager.create_car()
        creating_cars_6th_cycle = 0

    car_manager.move(scoreboard.level)

    for car in car_manager.car_array:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 260:
        scoreboard.level += 1
        player.setposition(0, -270)


screen.exitonclick()
