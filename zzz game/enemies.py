class Enemies:
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objects.")

    def is_alive(self):
        if self.hp < 1:
            return False

class OctoRock(Enemies):
    def __init__(self):
        self.hp = 30
        self.defense = 1
        self.attack = 2
