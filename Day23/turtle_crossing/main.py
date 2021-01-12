import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
ply = Player()
cars = CarManager()
screen.listen()
screen.onkey(ply.go_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.gen_car()
    cars.move_cars()
    # Detect Collision with cars
    for car in cars.all_cars:
        if car.distance(ply) < 20:
            game_is_on=False


    # Detecting successfull crossing
    if ply.is_at_finish():
        
        ply.go_to_start()



screen.exitonclick()