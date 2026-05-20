from turtle import Turtle
import utils

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.load_high_score()

        self.hideturtle()
        self.penup()
        self.goto(0, utils.SCREEN_WIDTH / 2 - utils.OFFSET_SCOREBOARD)
        self.pencolor("White")


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=utils.ALIGNMENT, font=utils.FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def restart_game(self):
        self.high_score = max(self.high_score, self.score)
        self.score = 0
        self.update_scoreboard()

    def print_game_over(self):
        self.goto(0, utils.SCREEN_HEIGHT / 4)
        self.write("Game Over.", align=utils.ALIGNMENT, font=utils.FONT_GAMEOVER)

    def save_high_score(self):
        with open(utils.FILENAME, "w") as file:
            file.write(str(self.high_score))

    def load_high_score(self):
        try:
            with open(utils.FILENAME) as file:
                return int(file.read())
        except FileNotFoundError:
            return 0