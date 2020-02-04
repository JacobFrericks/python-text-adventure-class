class Weopon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def get_attack(self):
        return self.attack

class DinkyWoodenBabySword(Weopon):
    def __init__(self):
        self.attack = 1

class ManlyBabySword(Weopon):
    def __init__(self):
        self.attack = 3