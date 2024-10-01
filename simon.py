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
    
    """
Adds a random number between 0-4 to the list
"""
    
def on_off(name):
    name.value = True
    time.sleep(0.3)
    name.value = False
    time.sleep(0.3)
    
"""
Makes the LED light blink

"""

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
            
"""
For the number of items in the list it turns on the light that corresponds with the number in lst
"""

def user_sequence(lst):
    if blue_button.value:
         lst.append(3)
    if yellow_button.value:
         lst.append(2)
    if green_button.value:
         lst.append(1)
    if red_button.value:
        lst.append(0)
    
"""
Adds the values in the list based of the user's input. Depending on what button that is pressed it adds that number to the list.

"""

def reset():
    game_start = False
    print(game_start)
    the_list = []
    print(the_list)
    user_list = []
    display_score()
    print(score)
    
    """
Sets game_start to false

Set's simions list to empty

Set's user list to empty

Display's the user score
    """
    
def display_score():
    ones = score % 10
    tens = score / 10
    for i in range(tens):
        on_off(green)
    for j in range (ones):
        on_off(red)
    
    """
Supposed to display the final score with the first leds on the right hand side of my board by using the green light as the tens
place and the red light as the ones place.
    """
        
def check_list(lst_one, lst_two):
    global score
    
    for i in range(len(lst_one)):
        if lst_one[i] == lst_two[i]:
            score = score + 1
            print("yes")
        else:
            reset()
            print("no")
"""
Has the score as a global varible so it'll change outside of the function

Goes through a loop for how evere many number of values is in the first list

    if the value of the first list matches the value of the second list
        then it'll update the score by 1
    if the values of those list doesnt match up then it calls the function reset()

"""
    
        
the_list = []
user_list = []
game_start = False
score = 0

while True:
    if white_button.value:
        add_to_sequence(the_list)
        print(the_list)
        display_sequence(the_list)
        #pass
    if blue_button.value or green_button.value or yellow_button.value or red_button.value:
        user_sequence(user_list)
        print(user_list)
        display_sequence(user_list)
        time.sleep(0.2)
        check_list(the_list, user_list)
        pass
