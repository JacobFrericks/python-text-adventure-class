# Learn about objects
from random import randint

# This is an object. Mario has hp and coins for properties
class Mario:
    def __init__(self, hp, coins):
        self.hp = hp
        self.coins = coins

# This is how you use the object
mario = Mario(100, 100)

door1 = randint(0, 50)
door2 = randint(0, 75)
door3 = randint(0, 100)

choice = int(input("Door 1, door 2, door 3? "))
print("Entering door", choice)

if choice == 1:
    # This is how you use the properties of the object
    mario.coins = mario.coins - door1
    print("Took away", door1, "coins. You now have", mario.coins, "coins.")

    door4 = randint(0, 20)
    door5 = randint(0, 50)
    door6 = randint(0, 30)

    choice = int(input("Door 4, door 5, door 6? "))

    if choice == 4:
        mario.coins = mario.coins - door4
        print("Took away", door4, "coins. You now have", mario.coins, "coins.")
        mario.hp = mario.hp - randint(0, 30)

        door7 = "bowser"
        door8 = "princess"
        choice = int(input("Door 7 or door 8? "))

        if choice == 7:
            print("It's bowser! Go get 'em")
            mario.hp = mario.hp - randint(1, 100)
            if mario.hp < 0:
                print("You lose!")
            else:
                print("Congratulations! You saved the princess!")
                print("Score:", mario.coins)
        if choice == 8:
            print("Congratulations! You saved the princess!")
            print("Score:", mario.coins)

    if choice == 5:
        mario.coins = mario.coins - door6
        print("You fall through a trap door and get put in prison.")

    if choice == 6:
        mario.coins = mario.coins - door6
        print("You fall through a trap door and get put in prison.")

if choice == 2:
    print("Entered door 2")
    mario.coins = mario.coins - door2
    mario.hp = 0
    print("You trip and break your arm. You can't continue, and so you exit the castle until you heal")

if choice == 3:
    mario.coins = mario.coins - door3
    print("Took away", door3, "coins. You now have", mario.coins, "coins.")
    print("You step on a trap and get burned alive")
    mario.hp = 0
