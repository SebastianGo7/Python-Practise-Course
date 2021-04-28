from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]

    def add_part(self, position):
        snake_part = Turtle()
        snake_part.color("white")
        snake_part.shape("square")
        snake_part.penup()
        snake_part.setposition(position)
        self.snake_parts.append(snake_part)

    def extend(self):
        self.add_part(self.snake_parts[-1].position())

    def create_snake(self):
        for position in POSITIONS:
            self.add_part(position)

    def move(self):
        for part_num in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[part_num - 1].xcor()
            new_y = self.snake_parts[part_num - 1].ycor()
            self.snake_parts[part_num].goto(new_x, new_y)

        self.snake_parts[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
