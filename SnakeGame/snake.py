from turtle import Screen, Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP=90
DOWN=270
LEFT=180
RIGHT=0

# Step 3 Move all snake code to OOP classes and then use
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(i)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()

            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    # Step 4 Listen to keyboard and move the snake
    def up(self):
        # self.segments[0].seth(90)
        # CODE TO RESTRICT CNAKE FROM MOVING BOTH SIDES / MAKING THE SNAKE ONE SIDED
        if self.head.heading() != DOWN:
            self.head.seth(UP)



    def down(self):
        # self.segments[0].seth(270)
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        # self.segments[0].seth(180)
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        # self.segments[0].seth(0)
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
