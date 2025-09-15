import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.penup()
        self.color("green")
        self.random_position()

    def random_position(self):
        random_x = random.randint(-285, 285)
        random_y = random.randint(-275, 275)
        self.goto(random_x, random_y)