from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.seth(90)
        self.goto(0,-280)
    def go_forward(self):
        self.forward(MOVE_DISTANCE)
