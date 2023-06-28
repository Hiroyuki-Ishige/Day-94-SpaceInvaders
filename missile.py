import turtle
from turtle import Turtle

import time

MISSILE_MOVE_DISTANCE = 10
MISSILE_COLOUR = "white"

turtle.register_shape("./image/missile.gif")


class Missile_player(Turtle):
    def __init__(self, x, y,):
        super().__init__()
        self.hideturtle()
        self.shape("./image/missile.gif")
        self.penup()
        self.fillcolor(MISSILE_COLOUR)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.setpos(x, y)
        self.status = "missile_on"
        self.showturtle()

        # self.missile_hit_judge(all_invaders)

    def missile_move(self,):
        # missile_is_on = True
        y_dir = MISSILE_MOVE_DISTANCE
        while self.ycor() <350:

            self.goto(self.xcor(), self.ycor() + y_dir)

    def missile_hit(self, all_invaders):
            for invader in all_invaders:
                if invader.distance(self) < 20:
                    all_invaders.remove(invader)
            # else:
            #     missile_is_on = False



