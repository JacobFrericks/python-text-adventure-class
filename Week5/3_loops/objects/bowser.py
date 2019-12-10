from random import randint

class Bowser:
    def __init__(self):
        self.damage = 25
        self.hp = 50

    def attack(self):
        return randint(0, self.damage)
