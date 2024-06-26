from karel.stanfordkarel import *
"""
Karel should fill the whole world with beepers - Ibtisam
"""
def main():
    run()
    return_back()

def run():
	put_beeper()
	completeEastLine()
	
def completeEastLine():
	alternateToWall()
	turn_left()
	if front_is_clear():
		startNextLine()
		turn_left()
		completeWestLine()
	
def completeWestLine():
	alternateToWall()
	turn_right()
	if front_is_clear():
		startNextLine()
		turn_right()
		completeEastLine()
	
def startNextLine():
	if beepers_present():
		move()
		
	else:
		move()
		put_beeper()

def alternateToWall():
	while front_is_clear():
		if beepers_present():
			move()
			
		else:
			move()
			put_beeper()
  

def return_back():
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_right()
    while front_is_clear():
        move()

    turn_right()
    turn_right()


def turn_right():
    turn_left()
    turn_left()
    turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
