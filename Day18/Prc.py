import turtle as t
import random

tim = t.Turtle()


# timmy_the_turtle.shape("circle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.dot(19)
#
# timmy_the_turtle.forward(100)
#
# # Drawing a square using turtle
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# # Dashed line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# shapes
# # Triangle
# tim.forward(100)
# tim.right(120)
# tim.forward(100)
# tim.right(120)
# tim.forward(100)
# # Square
# tim.right(120)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)

# to change color to random
# def change_color(t):
#     R = random.random()
#     B = random.random()
#     G = random.random()
#
#     return t.color(R, G, B)
#
#
# #
# #
# #
# # for i in range(3, 8):
# #     change_color(tim)
# #
# #     for _ in range(i):
# #         tim.forward(100)
# #         tim.right(360/i)
# # random walk
# direction=[0,90,180,270]
# # tim.width(random.randint(1,15))
# tim.pensize(15)
# tim.speed(0)   # we can give even "fastest" or "fast" etc
# for i in range(50):
#
#     change_color(tim)
#     tim.forward(50)
#     # tim.right(random.randint(0,270,90))
#     # tim.forward(random.randint(0,10))
#     # tim.left(random.randint(0,90))
#     tim.setheading(random.choice(direction))
#

# tuples are not changeable / immutable
# t.colormode(255)
#
#
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


t.colormode(255)
tim.speed("fastest")


def draw_spirograph(size_ofgap):
    for _ in range(int(360 / size_ofgap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_ofgap)


draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()
