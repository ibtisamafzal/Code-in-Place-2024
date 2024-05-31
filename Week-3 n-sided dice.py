import random

def main():
    dice = int (input("How many sides does your dice have? "))
    die = random.randint(1, dice)
    print ("Your roll is " +str(die))

if __name__ == '__main__':
    main()
