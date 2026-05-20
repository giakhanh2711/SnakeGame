SQUARE_SIZE = (1, 1)
FOOD_SIZE = (0.5, 0.5)

#==== Screen ====
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

#==== Snake ====
STEP = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

COLLIDE_DISTANCE = 15
OFFSET_COLLISION_EDGES = 9

#==== Food ====
OFFSET = 10 # Food offset to random location with edges

#==== ScoreBoard ====
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
OFFSET_SCOREBOARD = 40
FONT_GAMEOVER = ("Courier", 25, "normal")
FILENAME = "high_score.txt"

def yes_no_playing(screen):
    is_play = ""
    while is_play.lower() not in ["y", "yes", "no", "n"]:
        is_play = screen.textinput("Start playing.", "Type (y/yes or n/no): ")

    return is_play.lower()
