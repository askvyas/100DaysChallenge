# Step 5 Food in the game

from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super(Food, self).__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed(0) # or can be given as fastest
        random_x=random.randint(-280,280)
        random_y=random.randint(-280,280)
        self.goto(random_x,random_y)


