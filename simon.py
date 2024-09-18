import board
import random
from digitalio import DigitalInOut, Direction
import time


red = DigitalInOut(board.D2)
red.direction = Direction.OUTPUT

green = DigitalInOut(board.D3)
green.direction = Direction.OUTPUT

yellow = DigitalInOut(board.D4)
yellow.direction = Direction.OUTPUT

blue = DigitalInOut(board.D5)
blue.direction = Direction.OUTPUT


white = DigitalInOut(board.D6)
white.direction = Direction.INPUT
black = DigitalInOut(board.D7)
black.direction = Direction.INPUT
orange = DigitalInOut(board.D8)
orange.direction = Direction.INPUT

def add_to_sequence(lst):
    lst.append(random.randint(0, 3))
    
def on_off(name):
    name.value = True
    time.sleep(0.3)
    name.value = False
    time.sleep(0.3)

def display_sequence(lst):
    for x in lst:
        if x == 0:
            on_off(red)
        if x == 1:
            on_off(green)
        if x == 2:
            on_off(yellow)
        if x == 3:
            on_off(blue)

the_list = []

while True:
    ##print("Add to Sequence (Press white button)")
    #print("Display Sequence (Press black button)")
    #print("Exit Program (Press orange button)")
    if white.value == True:
        add_to_sequence(the_list)
    elif black.value == True:
        display_sequence(the_list)
    elif orange.value == True:
        the_list = []
