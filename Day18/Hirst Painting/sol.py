import turtle as turtle_module
import random
turtle_module.colormode(255)
tim=turtle_module.Turtle()
tim.speed(0)
new_color = [(237, 36, 111), (150, 24, 66), (215, 167, 53), (8, 146, 90), (240, 72, 34), (186, 161, 41), (27, 127, 194),
             (47, 190, 233), (245, 219, 49), (181, 38, 100), (81, 24, 87), (126, 192, 92), (252, 225, 0),
             (22, 170, 125), (219, 57, 21), (213, 133, 169), (147, 26, 22), (21, 191, 223), (233, 164, 196),
             (240, 168, 159), (0, 118, 49), (164, 211, 175), (132, 212, 231), (117, 3, 2), (49, 137, 208), (252, 8, 29)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_dots=100
for dot_counts in range(1,num_dots):
    tim.dot(20, random.choice(new_color))
    tim.forward(50)
    if dot_counts%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen=turtle_module.Screen()
screen.exitonclick()