from random import randint

class Goomba:
    def __init__(self):
        self.damage = 10

    # This is a function! We can use this in main.py, or in this class itself. Right now, the function doesn't save us from
    # duplicate code, but it will in the future! When we learn about loops, we will run this function several times!
    def attack(self):
        return randint(0, self.damage)
