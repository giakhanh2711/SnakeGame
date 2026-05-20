from turtle import Turtle, Screen
import time

import utils
from snake import Snake
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=utils.SCREEN_WIDTH, height=utils.SCREEN_HEIGHT)
screen.title("Snake Game")
screen.bgcolor("black")

is_play = utils.yes_no_playing(screen)
scoreboard = ScoreBoard()

while is_play in ["y", "yes"]:
    screen.clearscreen()
    screen.bgcolor("black")
    screen.tracer(0)

    scoreboard.restart_game()
    snake = Snake(3)
    food = Food()

    screen.listen()
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)

    while True:
        time.sleep(0.2)
        screen.update()

        snake.move()

        if snake.check_collide_edges() or snake.check_bite_tail():
            break

        if snake.check_collide_food(food):
            snake.eat_food()
            food.refresh()
            scoreboard.increase_score()

    is_play = utils.yes_no_playing(screen)

scoreboard.restart_game()
scoreboard.print_game_over()
scoreboard.save_high_score()
time.sleep(1)
