from random import randint

class Mario:
    def __init__(self, coins):
        self.coins = coins
        self.hp = 100
        self.damage = 20

    def attack(self):
        return randint(0,self.damage)