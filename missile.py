from turtle import Turtle
import time

MISSILE_MOVE_DISTANCE = 50
MISSILE_COLOUR = "white"


def shoot_missile(x=0, y=-300):
    missile = Missile_player(x, y) #TODO revise x, y so that to shoot missile from player's machine
    missile.shoot()


class Missile_player(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.hideturtle()
        self.shape("circle")
        self.penup()
        self.fillcolor(MISSILE_COLOUR)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.setpos(x, y)
        self.status = "missile_on"

    def shoot(self):
        y_dir = MISSILE_MOVE_DISTANCE
        self.showturtle()
        while self.status == "missile_on":
            self.goto(self.xcor(), self.ycor() + y_dir)
            if self.ycor() == 300:
                self.status = "missile_off"
