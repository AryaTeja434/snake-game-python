from turtle import Screen
import time
from snake import Snake
from food import Food
from score import ScoreBoard

screen=Screen()
screen.setup(width=600,height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)



game_on=True
snake=Snake()
food=Food()
score_board=ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Create new food and increase the snake
    if snake.head.distance(food) < 15:
        food.random_position()
        score_board.score+=1
        score_board.update_score()

        snake.extend_snake()

    #Detect the Wall Collision
    if snake.head.xcor()>285 or snake.head.xcor()<-285 or snake.head.ycor()>285 or snake.head.ycor()<-285:
        score_board.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()










screen.exitonclick()