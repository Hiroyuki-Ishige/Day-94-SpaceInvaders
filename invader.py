import turtle
from turtle import Turtle
import time
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
INVADER_ROW = 4  # How many rows to create
INVADER_COLUMN = 8 # How many blocks in horizontally (standard is 8)
INVADER_PLACE = random.randint(0, 50)  # set first block at left side

turtle.register_shape("./image/invader.gif")

class Invader:

    def __init__(self):
        self.all_invaders = []

    def create_invader(self):
        number_invaders = range(0, INVADER_COLUMN)
        rows = range(0, INVADER_ROW)

        for row in rows:
            for i in number_invaders:
                new_invader = Turtle("square")
                new_invader.shape("./image/invader.gif")
                new_invader.penup()
                new_invader.color(random.choice(COLORS))
                new_invader.shapesize(stretch_wid=1, stretch_len=3)
                new_invader.setpos(x=-250 + 20 + i * 65 + INVADER_PLACE, y=330 - 25 * row)
                self.all_invaders.append(new_invader)
                # print(self.all_blocks)
