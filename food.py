from turtle import Turtle
import utils
import random

class Food(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.shapesize(*utils.FOOD_SIZE)
        self.refresh()


    def refresh(self):
        half_width, half_high = int(utils.SCREEN_WIDTH / 2), int(utils.SCREEN_HEIGHT / 2)
        random_x = random.randint(utils.OFFSET - half_width, half_width - utils.OFFSET)
        random_y = random.randint(utils.OFFSET - half_high, half_high - utils.OFFSET)

        self.goto(random_x, random_y)