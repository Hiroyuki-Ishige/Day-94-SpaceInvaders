import json
import time
from datetime import datetime
from turtle import Screen, Turtle
from tkinter import *
from tkinter import messagebox
import pickle
import pprint

from player_mc import Player
from missile import Missile_player
from invader import Invader

# Fixed variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# making screen object
sc = Screen()
sc.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
sc.bgcolor("black")
sc.title("Space invaders")

# create initial screen --------------------------------
sc.tracer(0)  # Turn OFF screen update. 0 is off, 1 is on

# Create player
player = Player()

#------------------------------------------------------------
def shoot_missile():
    missile = Missile_player(x=player.xcor(), y=player.ycor())


# set key listen---------------------------------------
sc.listen()
sc.onkey(player.move_left, "z")
sc.onkey(player.move_right, "x")
sc.onkey(shoot_missile, "space")

# Ireate invader (temploally put on here)
invader = Invader()  # Create instance
invader.create_invader()

# game -------------------------------------------------------
game_is_on = True
while game_is_on:
    time.sleep(0.001)




    sc.tracer(1) # Turn ON screen update. 0 is off, 1 is on

sc.exitonclick()
# mainloop()

#TODO erase invader if missile hit
#TODO change invader design
#TODO Invader shoot missile
#TODO create UFO
#TODO judgement on hit(missile, Invader, UFO)
#TODO create game over
#TODO create Score board
#TODO next stage

