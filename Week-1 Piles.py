from karel.stanfordkarel import *

# File: piles.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel
# pick up all the beepers in the world.

def main():
    move()
    picker()
    mover()
    picker()
    mover()
    picker()
    move()

def mover():
    for i in range(2):
        move()
    
def picker():
    for i in range(10):
        pick_beeper()
    
   
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()