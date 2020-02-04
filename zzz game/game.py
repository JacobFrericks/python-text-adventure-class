from player import PlayerLink
import world

def play():
    player = PlayerLink()
    print(player.is_alive())
    if player.is_alive():
        tile = world.tile_at(player.x, player.y)
        print(tile.intro_text())

play()