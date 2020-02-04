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
        self.x = self.x + x
        self.y = self.y + y

    def move_up(self):
        self.movement(self.x, -1)

    def move_down(self):
        self.movement(self.x, 1)

    def move_left(self):
        self.movement(-1, self.y)

    def move_right(self):
        self.movement(1, self.y)

    def is_alive(self):
        if self.hp < 1:
            return False
        else:
            return True

    def inventory(self):
        print(self.inv)


