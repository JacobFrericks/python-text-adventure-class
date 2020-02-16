from player import Player
import world

def play():
    print("Escape from Cave Terror!")
    world.create_world()
    player = Player()
    while player.is_alive() and not player.victory:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        room.modify_player(player)
        if player.is_alive() and not player.victory:
            choose_action(room, player)
        elif not player.is_alive():
            print("Your journey has come to an early end!")


def choose_action(tile, player):
    action = None
    while not action:
        available_actions = get_available_actions(tile, player)
        action_input = input("Action: ")
        action = available_actions.get(action_input)
        if action:
            action()
        else:
            print("Invalid action!")

def get_available_actions(tile, player):
    actions = {}
    print("Choose an action: ")
    if isinstance(tile, world.EnemyTile) and tile.enemy.is_alive():
        action_adder(actions, 'a', player.attack, "Attack")
    else:
        if world.tile_at(tile.x, tile.y - 1):
            print(world.tile_at(tile.x, tile.y-1))
            action_adder(actions, 'u', player.move_up, "Go up")
        if world.tile_at(tile.x, tile.y + 1):
            action_adder(actions, 'd', player.move_down, "Go down")
        if world.tile_at(tile.x + 1, tile.y):
            action_adder(actions, 'r', player.move_right, "Go right")
        if world.tile_at(tile.x - 1, tile.y):
            action_adder(actions, 'l', player.move_left, "Go left")

    return actions

def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}: {}".format(hotkey, name))

play()