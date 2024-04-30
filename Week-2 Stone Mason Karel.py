from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    first_arch()
    second_arch()
    third_arch()
    second_arch()
    turn_left()
    

def first_arch():
    turn_left()
    while front_is_clear():
        put_beeper()
        move()
    
    put_beeper()

def second_arch():
    turn_right()
    for i in range(4):
        move()
    put_beeper()
    turn_right()
    while front_is_clear():
        move()
        put_beeper()

def third_arch():
    turn_left()
    for i in range(4):
        move()
    turn_left()
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
        
def turn_right():
    turn_left()
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()
