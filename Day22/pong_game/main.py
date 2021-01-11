from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
score=Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect the collision of the ball with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        # It needs to bounce

        ball.bounce_y()
    # To detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:

        print("Made Contact")
        ball.bounce_x()

    # Detect of Right paddle misses
    if ball.xcor() >380:
        score.l_point()
        score.update_scoreboard()


        ball.reset_position()

    if ball.xcor() < -380:
        score.r_point()
        score.update_scoreboard()
        ball.reset_position()
        score.r_score += 1



screen.exitonclick()
