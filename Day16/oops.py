# Lets use Turtle for understanding

from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("red")

my_screen = Screen()
# print(my_screen.canvheight)
timmy.forward(100)
timmy.left(100)
timmy.forward(100)
timmy.left(100)
timmy.forward(100)
timmy.left(100)
timmy.forward(100)
my_screen.exitonclick()
