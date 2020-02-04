import world
from Player import PlayerLink

def play():
    player = PlayerLink()
    if player.is_alive():
        tile = world.tile_at(PlayerLink.x, PlayerLink.y)
        print(tile.intro_text())

play()