# Game of US State Quiz
from turtle import Turtle,Screen
import  pandas as pd


# Turtle Setup
tut_gm=Turtle()
screen=Screen()
screen.bgpic(picname='blank_states_img.gif')
tut_gm.hideturtle()
tut_gm.penup()
# importing data
df = pd.read_csv("50_states.csv")
states = df["state"].to_list()

# Create a list of xcor and ycor from state name from pandas csv
loc=[]
for st in states:
    x_cor=int(df[df["state"]==st]['x'])
    y_cor=int(df[df["state"]==st]['y'])
    loc.append((x_cor,y_cor))


# Create a dictonary with state names and x_cor and y_cor
dict= {
    "State":states,
    "Location":loc
}
# Export this dataframe into a pandas


# Game in a loop
game_is_on=True
while game_is_on:
    state = screen.textinput("State Name", "Enter The State name")
    if state in states:
        ind=states.index(state)
        tut_gm.goto(loc[ind])
        tut_gm.write(state, True, align="center")

    else:
        break





screen.exitonclick()
