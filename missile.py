from turtle import Turtle

import time

MISSILE_MOVE_DISTANCE = 700
MISSILE_COLOUR = "white"


class Missile_player(Turtle,):
    def __init__(self, x, y):
        super().__init__()
        self.hideturtle()
        self.shape("circle")
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
            # if self.ycor() == 300:
            #     self.status = "missile_off"

    # def shoot(self):
    #     y_dir = MISSILE_MOVE_DISTANCE
    #     self.showturtle()
    #     while self.status == "missile_on":
    #         self.goto(self.xcor(), self.ycor() + y_dir)
    #         if self.ycor() == 300:
    #             self.status = "missile_off"
