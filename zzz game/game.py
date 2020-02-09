from player import PlayerLink
import world

def play():
    player = PlayerLink()
    while player.is_alive():
        tile = world.tile_at(player.x, player.y)
        print(tile.intro_text())
        tile.modify_player(player)

play()