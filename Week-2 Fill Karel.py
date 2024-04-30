from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""

def main():
    walk_to_end()
    while right_is_clear():
        move_to_next()
        walk_to_end()
    back_to_position()

def walk_to_end():
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()
    turn_left()
    turn_left()
    while front_is_clear():
        move()

def move_to_next():
    turn_right()
    move()
    turn_right()

def back_to_position():
    turn_right()
    turn_right()
    while front_is_clear():
        move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()




# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
