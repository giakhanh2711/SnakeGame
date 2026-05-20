from turtle import Turtle
import utils
from utils import OFFSET_COLLISION_EDGES


class Square(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(*utils.SQUARE_SIZE)
        self.penup()
        self.goto(x, y)
        self.color("white")

class Snake:
    def __init__(self, length):
        self.squares = []
        for i in range(length):
            self.squares.append(Square(-20 * i, 0))
        self.head = self.squares[0]
        self.previous_location_tail = self.squares[-1].position()

    def check_collide_food(self, food):
        return self.head.distance(food.position()) <= utils.COLLIDE_DISTANCE

    def move(self):
        self.previous_location_tail = self.squares[-1].position()
        for i in range(len(self.squares) - 1, 0, -1):
            self.squares[i].goto(self.squares[i - 1].position())
        self.head.forward(utils.STEP)

    def up(self):
        if self.head.heading() != utils.DOWN:
            self.head.setheading(utils.UP)

    def down(self):
        if self.head.heading() != utils.UP:
            self.head.setheading(utils.DOWN)

    def left(self):
        if self.head.heading() != utils.RIGHT:
            self.head.setheading(utils.LEFT)

    def right(self):
        if self.head.heading() != utils.LEFT:
            self.head.setheading(utils.RIGHT)

    def eat_food(self):
        # if self.check_collide_food():
        self.squares.append(Square(*self.previous_location_tail))

    def check_collide_edges(self):
        bound_x, bound_y = int(utils.SCREEN_WIDTH / 2), int(utils.SCREEN_HEIGHT / 2)
        if abs(self.head.xcor() - (-bound_x)) <= OFFSET_COLLISION_EDGES or \
            abs(self.head.xcor() - bound_x) <= OFFSET_COLLISION_EDGES or \
            abs(self.head.ycor() - (-bound_y)) <= OFFSET_COLLISION_EDGES or \
            abs(self.head.ycor() - bound_y) <= OFFSET_COLLISION_EDGES:
            return True

        return False

    def check_bite_tail(self):
        for square in self.squares[1:]:
            if self.head.distance(square.position()) <= 19:
                return True
        return False
