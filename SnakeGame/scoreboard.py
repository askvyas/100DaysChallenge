from turtle import Turtle


# Step 7 score card
ALIGNMENT= "center"
FONT=("Courier",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 270)
        self.penup()
        self.speed(0)
        self.ht()
        self.color("White")
        self.score = 0
        self.write(f"Score : {self.score}", move=False, align="center", font=("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", move=False, align="center", font=("Arial", 20, "normal"))
