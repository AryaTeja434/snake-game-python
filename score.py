from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt","r") as read_data:
            self.high_score=int(read_data.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_score()
        self.ht()

    def update_score(self):
        self.clear()
        self.write(f"Your Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score=self.score
            with open("data.txt","w") as write_data:
                write_data.write(f"{self.score}")
        self.score=0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align="center", font=("Arial", 30, "normal"))
