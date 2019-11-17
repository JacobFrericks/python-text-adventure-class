def play():
    print("Save the princess!")
    action_input = get_player_command()
    if action_input == '1':
        print("Door 1!")
    elif action_input == '2':
        print("Door 2!")
    elif action_input == '3':
        print("Door 3!")
    else:
        print("Invalid action!")

def get_player_command():
    return input('Door 1, Door 2, or Door 3? ')

play()

class Warrior:
    def __init__(self, weapon, armor, hp, damage):
        self.weapon = weapon
        self.armor = armor
        self.hp = hp
        self.damage = damage

    def attack(self):
        print("Attacked with " + self.weapon + "! Enemy took " + str(self.damage) + " damage!")

knight = Warrior("sword", "steel", 200, 150)
mario = Warrior("fireballs", "plumber outfit", 50, 50)
sumo_wrestler = Warrior("stomach", "none", 500, 200)

knight.attack()
mario.attack()
sumo_wrestler.attack()