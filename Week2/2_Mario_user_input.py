# Learn about random numbers, user input and objects
from random import randint

mario_coins = 100

door1 = randint(0, 50)
door2 = randint(0, 75)
door3 = randint(0, 100)

choice = int(input("Door 1, door 2, door 3? "))
print("Entering door", choice)

if choice == 1:
    mario_coins = mario_coins - door1
    print("Took away", door1, "coins. You now have", mario_coins, "coins.")

    door4 = randint(0, 20)
    door5 = randint(0, 50)
    door6 = randint(0, 30)

    choice = int(input("Door 4, door 5, door 6? "))

    if choice == 4:
        mario_coins = mario_coins - door4
        print("Took away", door4, "coins. You now have", mario_coins, "coins.")

        door7 = "bowser"
        door8 = "princess"
        choice = int(input("Door 7 or door 8? "))

        if choice == 7:
            print("Instead of the princess, you met bowser. You lose!")
        if choice == 8:
            print("Congratulations! You saved the princess!")
            print("Score:", mario_coins)

    if choice == 5:
        mario_coins = mario_coins - door6
        print("You fall through a trap door and get put in prison.")

    if choice == 6:
        mario_coins = mario_coins - door6
        print("You fall through a trap door and get put in prison.")

if choice == 2:
    print("Entered door 2")
    mario_coins = mario_coins - door2
    print("You trip and break your arm. You can't continue, and so you exit the castle until you heal")

if choice == 3:
    mario_coins = mario_coins - door3
    print("Took away", door3, "coins. You now have", mario_coins, "coins.")
    print("You step on a trap and get burned alive")
