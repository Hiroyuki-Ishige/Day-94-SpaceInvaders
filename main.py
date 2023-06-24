import json
import time
from datetime import datetime
from turtle import Screen, Turtle
from tkinter import *
from tkinter import messagebox
import pickle
import pprint

from player_mc import Player

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


# set key listen---------------------------------------
sc.listen()
sc.onkey(player.move_left, "Left")
sc.onkey(player.move_right, "Right")
#-------------------------------------------------------

sc.tracer(1) # Turn ON screen update. 0 is off, 1 is on

sc.exitonclick()
# mainloop()



#TODO create missile
#TODO create Invader (& missile from them)
#TODO create UFO
#TODO judgement on hit(missile, Invader, UFO)
#TODO create game over
#TODO create Score board
#TODO next stage

