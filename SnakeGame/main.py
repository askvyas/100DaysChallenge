from turtle import Turtle,Screen




screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")

#Step 1 Creating a snake
# Method 1
t1=Turtle("square")
t2=Turtle("square")
t3=Turtle("square")
t1.color("white")
t2.color("white")
t3.color("white")
t2.setpos(x=-20,y=0)
t3.setpos(x=-40,y=0)












screen.exitonclick()
