import turtle
from turtle import Turtle
import time

PLAYER_MOVE_DISTANCE = 40
PLAYER_WIDTH = 4
PLAYER_INITIAL_X = 0
PLAYER_INITIAL_Y = -330
PLAYER_COLOUR = "white"

turtle.register_shape("./image/cannon.gif")

class Player(Turtle):
    def __init__(self):
        super().__init__()  # inherit Turtle Class
        self.shape("./image/cannon.gif")
        self.fillcolor(PLAYER_COLOUR)
        self.shapesize(stretch_wid=1, stretch_len=PLAYER_WIDTH) #Standard turtle size is 20 pixcel x 20 pixcel
        self.setpos(PLAYER_INITIAL_X, PLAYER_INITIAL_Y)

    def move_left(self):
        new_x = self.xcor() - PLAYER_MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + PLAYER_MOVE_DISTANCE
        self.goto(new_x, self.ycor())