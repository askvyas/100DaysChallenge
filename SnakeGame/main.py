from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

#  Step 1 Creating a snake
# # Method 1
# # t1=Turtle("square")
# # t2=Turtle("square")
# # t3=Turtle("square")
# # t1.color("white")
# # t2.color("white")
# # t3.color("white")
# # t2.setpos(x=-20,y=0)
# # t3.setpos(x=-40,y=0)
# # Method 2
# starting_position = [(0, 0), (-20, 0), (-40, 0)]
# segments = []
#
# for i in starting_position:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(i)
#     segments.append(new_segment)
#
# # Step 2 move the snake on the screen
#
# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     for seg_num in range(len(segments) - 1, 0, -1):
#         new_x = segments[seg_num - 1].xcor()
#         new_y = segments[seg_num - 1].ycor()
#
#         segments[seg_num].goto(new_x, new_y)
#     segments[0].forward(20)
#     segments[0].left(90)

#
# new_segment_pos=[(0,20),(0,0),(0,-20)]
# r_pos=[(0,-20),(0,0),(0,20)]
# count=0
# for seg in segments:
#     seg.setpos(r_pos[count])
#     count+=1
#
# def turn_left(segments):
#     c_pos=segments[0].positon()
#     for seg in segments
snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Step 6 Detecting collision with food
    if snake.head.distance(food) < 15:
        print("Collided")
        food.refresh()
        # Step 9 To extend the snake
        snake.extend()

        score.increase_score()

    # Step 8 Detect Collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()


    # Step 10 Head tail collision
    # if head collides with any of the segment and if it is yes then end the game
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
