from random import randint

class Attack:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def attack(self):
        return randint(0, self.damage)