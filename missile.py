from turtle import Turtle
import time

MISSILE_MOVE_DISTANCE = 3
MISSILE_COLOUR = "white"

class Missile_player(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.fillcolor(MISSILE_COLOUR)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.setpos(x, y) #TODO test if this setpos is currect or should be move to shoot.
        self.status = "game_on"

    def shoot(self):
        y_dir = MISSILE_MOVE_DISTANCE


        self.goto(self.xcor(),self.ycor()+y_dir)