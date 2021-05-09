import random


# creating the list of all mahjong tiles in a game
def mahjong_tiles():
    c, p, b = "character", "pin", "bamboo"
    n, e, s, w = "north", "east", "south", "west"
    r, wh, g = "red", "white", "green"

    # characters, pins and bamboo each have 4 sets of 9 numbered tiles
    characters = [[c, 1], [c, 2], [c, 3], [c, 4], [c, 5], [c, 6], [c, 7], [c, 8], [c, 9]]
    pins = [[p, 1], [p, 2], [p, 3], [p, 4], [p, 5], [p, 6], [p, 7], [p, 8], [p, 9]]
    bamboo = [[b, 1], [b, 2], [b, 3], [b, 4], [b, 5], [b, 6], [b, 7], [b, 8], [b, 9]]
    # there are 4 wins with 4 sets of each
    winds = [[n, 0], [e, 0], [s, 0], [w, 0]]
    # there are 3 dragons with 3 sets of each
    dragons = [[r, 0], [wh, 0], [g, 0]]
    # all the tiles consists of 4 sets of every type of tile
    all_tiles = (characters + pins + bamboo + winds + dragons)*4
    return all_tiles


def starting_hand(tile_set=mahjong_tiles()):
    hand = []
    for _ in range(1, 15):
        random_index = random.randrange(len(tile_set))
        tile_set[random_index], tile_set[-1] = tile_set[-1], tile_set[random_index]
        random_tile = tile_set.pop()
        hand.append(random_tile)
    return hand


def hand_won(hand):
    character_list = []
    pin_list = []
    bamboo_list = []
    other_list = []
    for item in hand:
        if item[0] is "character":
            character_list.append(item)
        elif item[0] is "pin":
            pin_list.append(item)
        elif item[0] is "bamboo":
            bamboo_list.append(item)
        else:
            other_list.append(item)
    if 1 == 1 is True:
        return True
    return False


hand_won(starting_hand())
