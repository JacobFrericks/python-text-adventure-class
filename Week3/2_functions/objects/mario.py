from random import randint

class Mario:
    def __init__(self, hp, coins):
        self.hp = hp
        self.coins = coins
        self.damage = 20

    # This is a function! We can use this in main.py, or in this class itself. Right now, we don't use this function, but
    # Mario will attack more when we learn about loops!
    def attack(self):
        return randint(0,self.damage)