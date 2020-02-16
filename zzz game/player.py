import world

class Player:
    def __init__(self):
        self.hp = 50
        self.d = 10
        self.att = 5
        self.money = 1
        self.inv = []
        self.x = 1
        self.y = 1
        self.victory = False

    def movement(self, x, y):
        self.x = self.x + x
        self.y = self.y + y

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

    def attack(self):
        room = world.tile_at(self.x, self.y)
        enemy = room.enemy
        enemy.hp -= self.att
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

