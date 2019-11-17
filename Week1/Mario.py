# This is how you set integers to a variable. A Variable just gives this number a name so we can use it later
mario_coins = 100

door1 = 50
door2 = 75
door3 = 100

choice = 1

# If statements! The program will go into the code under the if statement if the condition is true.
# Below, we will only go into this if statement if choice is 1.
#
# Python is special with if statements! The code can tell when the if statement is done by the indentation.
# You can see the the other choices for door 2 and 3 are indented the same as this one.
if choice == 1:
    mario_coins = mario_coins - door1

    door4 = 20
    door5 = 50
    door6 = 30

    choice = 4

    if choice == 4:
        mario_coins = mario_coins - door4

        choice = 8
        # This is how you set strings to a variable. It's almost exactly the same as numbers, but it's surrounded with double quotes
        door7 = "bowser"
        door8 = "princess"

        if choice == 7:
            print(door7)
        if choice == 8:
            print(door8)
    if choice == 6:
        mario_coins = mario_coins - door6

if choice == 2:
    mario_coins = mario_coins - door2
if choice == 3:
    mario_coins = mario_coins - door3