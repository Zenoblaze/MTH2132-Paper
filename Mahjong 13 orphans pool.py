import random
import numpy as np
from matplotlib import pyplot as plt
from copy import deepcopy


# creating the list of all mahjong tiles in a game
def tile_pool(tiles_set):
    c, p, b = "character", "pin", "bamboo"
    n, e, s, w = "north", "east", "south", "west"
    r, wh, g = "red", "white", "green"
    # characters, pins and bamboo each have 4 sets of 9 numbered tiles
    characters = [[c, 2], [c, 3], [c, 4], [c, 5], [c, 6], [c, 7], [c, 8]]
    pins = [[p, 2], [p, 3], [p, 4], [p, 5], [p, 6], [p, 7], [p, 8]]
    bamboo = [[b, 2], [b, 3], [b, 4], [b, 5], [b, 6], [b, 7], [b, 8]]
    # there are 4 wins with 4 sets of each
    winds = [[n, 0], [e, 0], [s, 0], [w, 0]]
    # there are 3 dragons with 3 sets of each
    dragons = [[r, 0], [wh, 0], [g, 0]]
    terminals = [[c, 1], [c, 9], [p, 1], [p, 9], [b, 1], [b, 9]]
    # all the tiles consists of 4 sets of every type of tile
    all_tiles = (characters + pins + bamboo + winds + dragons + terminals)*4
    ideal_hand = terminals + dragons + winds
    for _ in range(136 - tiles_set):
        random_index = random.randrange(len(all_tiles))
        all_tiles[random_index], all_tiles[-1] = all_tiles[-1], all_tiles[random_index]
        all_tiles.pop()
    return all_tiles, ideal_hand


def will_win(hand, ideal_hand):
    current_hand = []
    for elem in ideal_hand:
        if elem in hand:
            hand.remove(elem)
            current_hand.append(elem)
    if all(elem in current_hand for elem in ideal_hand):
        for elem in ideal_hand:
            if elem in hand:
                return True
    return False


def play_game(turns):
    tile_set, win_condition = tile_pool(turns + 13)
    return will_win(tile_set, win_condition), turns


def find_average(iterations, turns):
    wins = 0
    games = 0
    for _ in range(iterations):
        if play_game(turns)[0] is True:
            wins += 1
            games += 1
        else:
            games += 1
    win_chance = wins/games
    print("If you take " + str(turns) + " turns.\nThe odds of winning are: " + str(win_chance*100) + "%")
    return win_chance


def plot_turns_vs_chance():
    chance_list = []
    turns_list = []
    for _ in range(18, 136):
        turns_list.append(_)
    for turn in turns_list:
        chance_list.append(find_average(100000, turn))
    plt.plot(turns_list, chance_list)
    plt.xlabel("Turns taken")
    plt.ylabel("Probability of winning")
    plt.title("Probability of winning a 13-orphans hand")
    plt.show()


plot_turns_vs_chance()
