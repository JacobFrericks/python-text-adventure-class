import world

class PlayerLink:
    def __init__(self):
        self.hp = 50
        self.d = 10
        self.att = 5
        self.money = 1
        self.inv = []
        self.x = 1
        self.y = 1

    def movement(self, x, y):
        print("DX: " + str(x))
        print("DY: " + str(y))
        print("Old Location: (" + str(self.x) + ", " + str(self.y) + ")")
        self.x = self.x + x
        self.y = self.y + y
        print("New Location: (" + str(self.x) + ", " + str(self.y) + ")")

    def move_up(self):
        self.movement(0, -1)

    def move_down(self):
        self.movement(0, 1)

    def move_left(self):
        self.movement(-1, 0)

    def move_right(self):
        self.movement(1, 0)

    def is_alive(self):
        if self.hp < 1:
            return False
        else:
            return True

    def inventory(self):
        print(self.inv)

    def attack(self):
        room = world.tile_at(self.x, self.y)
        enemy = room.enemy
        print("BEFORE ENEMY HP: " + str(enemy.hp))
        enemy.hp -= self.att
        print("AFTER ENEMY HP: " + str(enemy.hp))
        print("SELF ATT: " + str(self.att))
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

