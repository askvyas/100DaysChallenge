# import colorgram
import turtle as t
import random

# colors = colorgram.extract('image.jpg', 30)
# l = []
# for i in range(0, 30):
#     tpl = (colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b)
#     l.append(tpl)
# print(l)
tim = t.Turtle()
t.colormode(255)

new_color = [(237, 36, 111), (150, 24, 66), (215, 167, 53), (8, 146, 90), (240, 72, 34), (186, 161, 41), (27, 127, 194),
             (47, 190, 233), (245, 219, 49), (181, 38, 100), (81, 24, 87), (126, 192, 92), (252, 225, 0),
             (22, 170, 125), (219, 57, 21), (213, 133, 169), (147, 26, 22), (21, 191, 223), (233, 164, 196),
             (240, 168, 159), (0, 118, 49), (164, 211, 175), (132, 212, 231), (117, 3, 2), (49, 137, 208), (252, 8, 29)]
tim.color(255,255,255)
tim.setpos(-300,-300)
flag=True
for i in range(10):
    for j in range(10):
        tim.color(random.choice(new_color))
        tim.dot(20)
        tim.penup()
        tim.forward(50)
        tim.pendown()
    if(flag):
        tim.left(90)
        tim.penup()
        tim.forward(50)
        tim.left(90)
        flag=False
    else:
        tim.right(90)
        tim.penup()
        tim.forward(50)
        tim.right(90)
        flag = True







print(tim.pos())
screen = t.Screen()
print(screen.window_height())




screen.exitonclick()
