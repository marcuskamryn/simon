import random

def add_to_sequence(lst):
    num = random.randint(0, 3)
    lst.append(num)

def display_sequence(lst):
    for x in lst:
        if x == 0:
            print("Red")
        if x == 1:
            print("Green")
        if x == 2:
            print("Yellow")
        if x == 3:
            print("Blue")

list = []

while True:
    print("Add to Sequence")
    print("Display Sequence")
    print("Exit Program")
    user = input("Type 'A', 'D', or 'E': ")
    if user == "A":
        add_to_sequence(list)
    elif user == "D":
        display_sequence(list)
    elif user == "E":
        break
