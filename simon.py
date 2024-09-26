import board
import random
from digitalio import DigitalInOut, Direction
import time


blue = DigitalInOut(board.D2)
blue.direction = Direction.OUTPUT

yellow = DigitalInOut(board.D3)
yellow.direction = Direction.OUTPUT

green = DigitalInOut(board.D4)
green.direction = Direction.OUTPUT

red = DigitalInOut(board.D5)
red.direction = Direction.OUTPUT


blue_button = DigitalInOut(board.D6)
blue_button.direction = Direction.INPUT
yellow_button = DigitalInOut(board.D7)
yellow_button.direction = Direction.INPUT
green_button = DigitalInOut(board.D8)
green_button.direction = Direction.INPUT
red_button = DigitalInOut(board.D9)
red_button.direction = Direction.INPUT
white_button = DigitalInOut(board.D10)
white_button.direction = Direction.INPUT

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

def user_sequence(lst):
    if blue_button.value:
         lst.append(3)
    if yellow_button.value:
         lst.append(2)
    if green_button.value:
         lst.append(1)
    if red_button.value:
        lst.append(0)

def reset():
    game_start = False
    the_list = []
    user_list = []
    display_score()
    
def display_score():
    ones = score % 10
    tens = score / 10
    for i in range(tens):
        on_off(green)
    for j in range (ones):
        on_off(red)
        
def check_list(lst_one, lst_two):
    pass
        

the_list = []
user_list = []
global game_start = False
global score = 0

while True:
    if white_button.value:
        add_to_sequence(the_list)
        display_sequence(the_list)
        pass
        
