# Learn about functions
from random import randint
from objects.mario import Mario
from objects.goomba import Goomba
from objects.bowser import Bowser


# Remember functions? We have so many print statements now, we're going to have the user press enter for each print!
def user_print(string):
    input(string)

mario = Mario(100)

door1 = randint(0, 50)
door2 = randint(0, 75)
door3 = randint(0, 100)

choice = int(input("Door 1, door 2, door 3? "))
print("Entering door", choice)

if choice == 1:
    mario.coins = mario.coins - door1
    print("Took away", door1, "coins. You now have", mario.coins, "coins.")

    door4 = randint(0, 20)
    door5 = randint(0, 50)
    door6 = randint(0, 30)

    choice = int(input("Door 4, door 5, door 6? "))

    if choice == 4:
        user_print("A Goomba appeared behind the door!")
        goomba = Goomba()
        # A while loop allows fights to happen!
        while goomba.hp > 0 and mario.hp > 0:
            damage = goomba.attack()
            mario.hp = mario.hp - damage
            # The str function turns an int into a string. That way we can pass in one string into our function
            user_print("The Goomba took away " + str(damage) + " hp. You now have " + str(mario.hp) + " health!")
            if mario.hp > 0:
                damage = mario.attack()
                goomba.hp = goomba.hp - damage
                user_print("Mario attacked the goomba! Mario took away " + str(damage) + "hp. The Goomba now has " + str(goomba.hp) + " health!")
        if mario.hp < 0:
            print("You lose! Try again!")
        else:
            print("The Goomba was defeated!")
            door7 = "bowser"
            door8 = "princess"
            user_print("You see one door ahead at the end of a long hallway. You slowly enter.")
            user_print("It's bowser! Go get 'em!")

            bowser = Bowser()
            while bowser.hp > 0 and mario.hp > 0:
                damage = bowser.attack()
                mario.hp = mario.hp - damage
                user_print("Bowser took away " + str(damage) + " hp. You now have " + str(mario.hp) + " health!")
                if mario.hp > 0:
                    damage = mario.attack()
                    bowser.hp = bowser.hp - damage
                    user_print("Mario attacked Bowser! Mario took away " + str(damage) + "hp. Bowser now has " + str(bowser.hp) + " health!")
            if mario.hp < 0:
                print("You lose! Try again!")
            else:
                print("You jumped over Bowser and cut the cable to the bridge he was standing on!")
                print("Bowser fell down a pit, never to be seen again!")
                print("Congratulations! You saved the princess!")
                print("Score:", mario.coins + mario.hp)

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
