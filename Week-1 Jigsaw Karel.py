from karel.stanfordkarel import *

"""
Karel should finish the puzzle by picking up the last beeper 
(puzzle piece) and placing it in the right spot. Karel should 
end in the same position Karel starts in -- the bottom left 
corner of the world.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while front_is_clear():
        take_beeper()
        move()

    set_position()
    put_beeper()
    turn_around()
    move()
    turn_right()
    while front_is_clear():
        move()
    
    turn_left()
    move() 
    turn_left()

def take_beeper():
    if beepers_present():
        pick_beeper()

def set_position():
    turn_left()
    move()
    turn_left()
    move()
    move()
    move()
    turn_right()
    move()

def turn_around():
    turn_right()
    turn_right()

def turn_right():
    for i in range(3):
        turn_left()



# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
