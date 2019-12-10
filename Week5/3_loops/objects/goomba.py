from random import randint

class Goomba:
    def __init__(self):
        self.damage = 10
        self.hp = 10

    def attack(self):
        return randint(0, self.damage)
