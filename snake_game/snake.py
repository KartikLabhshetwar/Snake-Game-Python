from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.new_segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.new_segments) - 1, 0, -1):
            new_x = self.new_segments[seg_num - 1].xcor()
            new_y = self.new_segments[seg_num - 1].ycor()
            self.new_segments[seg_num].goto(new_x, new_y)
        self.new_segments[0].forward(MOVE_DISTANCE)

    def add_segment(self, position):
        my_turtle = Turtle(shape="square")
        my_turtle.color("white")
        my_turtle.penup()
        my_turtle.goto(position)
        self.new_segments.append(my_turtle)

    def extend(self):
        self.add_segment(self.new_segments[-1].position())

    def up(self):
        if self.new_segments[0].heading() != DOWN:
            self.new_segments[0].setheading(UP)

    def down(self):
        if self.new_segments[0].heading() != UP:
            self.new_segments[0].setheading(DOWN)

    def right(self):
        if self.new_segments[0].heading() != LEFT:
            self.new_segments[0].setheading(RIGHT)

    def left(self):
        if self.new_segments[0].heading() != RIGHT:
            self.new_segments[0].setheading(LEFT)
