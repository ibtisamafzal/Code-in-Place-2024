from karel.stanfordkarel import *

# File: shelter.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel 
# move to the beeper, pick it up, and
# return home.

def main():
    find_wall()
    reverse()

def find_wall():
    while front_is_clear():
        move()
    if front_is_blocked():
        turn_right()
        move()
        turn_left()
        move()
        pick_beeper()

def reverse():
    for i in range(2):
        turn_left()
    move()
    turn_right()
    move()
    turn_left()
    while front_is_clear():
        move()
    if front_is_blocked():
        for j in range(2):
            turn_right()
    
def turn_right():
    for i in range(3):
        turn_left()

    
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()