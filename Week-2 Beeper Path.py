from karel.stanfordkarel import *

def main():
    check_beeper()

def check_beeper():
    while beepers_present():
        move()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()