import turtle
from turtle import Turtle

import time

MISSILE_MOVE_DISTANCE = 700
MISSILE_COLOUR = "white"

turtle.register_shape("./image/missile.gif")


class Missile_player(Turtle):
    def __init__(self, x, y,all_invaders):
        super().__init__()
        self.hideturtle()
        self.shape("./image/missile.gif")
        self.penup()
        self.fillcolor(MISSILE_COLOUR)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.setpos(x, y)
        self.status = "missile_on"
        # self.shoot()
        y_dir = MISSILE_MOVE_DISTANCE
        self.showturtle()
        # while self.status == "missile_on":
        self.goto(self.xcor(), self.ycor() + y_dir)
        self.missile_hit_judge(all_invaders)

    def missile_hit_judge(self, all_invaders):
        missile_is_on=True

        while missile_is_on:
            for invader in all_invaders:
                if invader.distance(self)<5:
                    all_invaders.remove(invader)