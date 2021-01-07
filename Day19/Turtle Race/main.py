from turtle import Turtle, Screen
import random as rd

timmy = Turtle()

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bets", prompt="Which turtle will win the race , enter colour")
colors = ["red", "blue", "green", "black", "violet", "pink", "brown"]

# turt1.color("red")
# turt2.color("green")
# turt3.color("blue")
#
# turt1.penup()
# turt2.penup()
# turt3.penup()
#
# turt1.goto(x=-230,y=-50)
# turt2.goto(x=-230,y=0)
# turt3.goto(x=-230,y=50)
l = []
for _ in range(0, 7):
    tmpTur = Turtle("turtle")
    tmpTur.penup()
    l.append(tmpTur)
x = -230
y = -150
for i in range(0, 7):
    l[i].color(colors[i])
    l[i].goto(x, y)
    y = y + 50

print(l[0].pos()[0])
flag = True
win=""
while flag :
    for i in range(0,7):
        l[i].forward(rd.randint(1, 15))
        if l[i].pos()[0] >= 230 :
            win=l[i].color()
            flag=False

print(f"the winner is {win} ")

screen.exitonclick()
