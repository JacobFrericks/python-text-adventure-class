from attack import Attack

class Bowser:
    # Technically we don't need a list here, since we just have one item in our list
    # But this allows us to add more attacks later if we want to
    attacks = [Attack("Flamethrower", 50)]

    def __init__(self):
        self.damage = 100

    def attack(self):
        return self.attacks[0].attack()
