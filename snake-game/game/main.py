import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()


is_game_on = True
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    snake.speed("slowest")

    if(snake.head.distance(food) < 15):
        food.refresh()

        score.increaseScore()
        score.screen.update()
        snake.extend()

    if(snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280):
        snake.reset()
        score.reset()

    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         is_game_on = False
    #         score.endgame()

    for segment in snake.segments[1: ]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()
