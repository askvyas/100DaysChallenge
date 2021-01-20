# Game of US State Quiz
from turtle import Turtle,Screen
import pandas as pd

# Font Constant Declaration
font=("Arial",10,"normal")


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
    x_cor=df[df["state"]==st]['x'].astype(int)
    y_cor=df[df["state"]==st]['y'].astype(int)
    loc.append((x_cor,y_cor))

# Not required
# # Create a dictonary with state names and x_cor and y_cor
# dict= {
#     "State":states,
#     "Location":loc
# }
# Export this dataframe into a pandas


# Game in a loop
# Adding a guessed states
guessed_states=[]
game_is_on=True
while game_is_on:
    state = screen.textinput("State Name", "Enter The State name").title()
    # Additional Exit Code added and states that we did not guess
    if state=="Exit":
        # Adding List Comprehension
        missing_states = [st for st in states if st not in guessed_states]

        # for s in states:
        #     if s not in guessed_states:
        #         missing_states.append(s)
        print(missing_states)
        game_is_on=False
    if state in states:

        ind=states.index(state)
        tut_gm.goto(loc[ind])
        tut_gm.write(state, True, align="center",font=font)
        guessed_states.append(state)








