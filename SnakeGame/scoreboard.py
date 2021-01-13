from turtle import Turtle

# Step 7 score card
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.goto(0, 270)
        self.penup()
        self.speed(0)
        self.ht()
        self.color("White")
        self.updat_score()

    def updat_score(self):
        self.clear()
        self.write(f"Score : {self.score}  High Score {self.high_score}", move=False, align="center",
                   font=("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.updat_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", move=False, align="center", font=("Arial", 20, "normal"))
    def reset(self):
        if self.score > self.high_score:
            self.high_score=self.score
            with open("data.txt", mode='w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.updat_score()
