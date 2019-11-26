from attack import Attack

class Mario:
    # Here we have a list of attacks!
    attacks = [Attack("Jump", 10), Attack("Fireball", 30)]

    def __init__(self, hp, coins):
        self.hp = hp
        self.coins = coins
        self.damage = 20

    def attack(self, name):
        return self.get_attack_by_name(name).attacks()

    def get_attack_by_name(self, name):
        # We can clean this up when we learn about maps! For now, we can do this with if statements
        if name == "Fireball":
            return self.attacks[1]
        else:
            return self.attacks[0]