from turtle import Turtle, Screen
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# screen.tracer(0)
# Step 1 Creating a snake
# Method 1
# t1=Turtle("square")
# t2=Turtle("square")
# t3=Turtle("square")
# t1.color("white")
# t2.color("white")
# t3.color("white")
# t2.setpos(x=-20,y=0)
# t3.setpos(x=-40,y=0)
starting_position = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for i in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(i)
    segments.append(new_segment)

# Step 2 move the snake on the screen

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg in segments:
        seg.forward(5)
        seg.setheading(90)

new_segment_pos=[(0,20),(0,0),(0,-20)]
r_pos=[(0,-20),(0,0),(0,20)]
count=0
for seg in segments:
    seg.setpos(r_pos[count])
    count+=1






screen.exitonclick()
