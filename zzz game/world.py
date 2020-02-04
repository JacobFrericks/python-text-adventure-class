START_X = 1
START_Y = 1

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        return ""

    def modify_player(self):
        return ""

world = [
    ["x", "x", "x", "e"],
    ["e", "s", "e", "x"],
    ["x", "x", "e", "v"]
]

start_location = 1, 1

def tile_at(x, y):
    tile = world[y][x]
    if tile == "x":
        return EmptyTile(x, y)
    if tile == "e":
        return EnemyTile(x, y)
    if tile == "v":
        return VicTile(x, y)
    if tile == "s":
        return StartTile(x, y)

class StartTile(MapTile):
    def intro_text(self):
        return "a world that seem dangerous"

class EnemyTile(MapTile):
    def intro_text(self):
        return "ow a octorock appeared"

    def modify_player(self):
        return "link lost 5hp"

    # super(1, 1).__init__()

class VicTile(MapTile):
    def intro_text(self):
        return "you win! nothing..."

class EmptyTile(MapTile):
    def intro_text(self):
        return ""

