import random
import numpy as np
from copy import deepcopy


# creating the list of all mahjong tiles in a game
def mahjong_tiles():
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
    return all_tiles, ideal_hand


def starting_hand():
    mahjong = mahjong_tiles()
    hand = []
    ideal_hand = mahjong[1]
    tile_set = mahjong[0]
    for _ in range(1, 15):
        random_index = random.randrange(len(tile_set))
        tile_set[random_index], tile_set[-1] = tile_set[-1], tile_set[random_index]
        random_tile = tile_set.pop()
        hand.append(random_tile)
    return hand, tile_set, ideal_hand


def turn(hand, tile_set, ideal_hand):
    pairs = []
    triples = []
    dupe_pair = False
    pair = False
    triple = False
    for elem in hand:
        if elem in ideal_hand:
            if hand.count(elem) > 1:
                pairs.append(elem)
            if hand.count(elem) > 2:
                triple = True
                triples.append(elem)
    for elem in pairs:
        if pairs.count(elem) > 1:
            pairs.remove(elem)
    for elem in triples:
        if triples.count(elem) > 1:
            triples.remove(elem)
    if len(pairs) >= 1:
        pair = True
    if len(pairs) > 1:
        dupe_pair = True
        pair = True
    random_index = random.randrange(len(tile_set))
    tile_set[random_index], tile_set[-1] = tile_set[-1], tile_set[random_index]
    random_tile = tile_set.pop()
    if random_tile in ideal_hand:
        if dupe_pair is True:
            hand.append(random_tile)
            for elem in hand:
                if elem in pairs:
                    hand.remove(elem)
                    break
        elif triple is True:
            hand.append(random_tile)
            for elem in hand:
                if elem in triples:
                    hand.remove(elem)
                    break
        elif random_tile not in hand or pair is False:
            hand.append(random_tile)
            for elem in hand:
                if elem not in ideal_hand:
                    hand.remove(elem)
                    break
    return hand, tile_set, ideal_hand


def has_won(hand, ideal_hand):
    hand_copy = deepcopy(hand)
    for elem in ideal_hand:
        if elem in hand_copy:
            hand_copy.remove(elem)
    if len(hand_copy) == 1 and hand_copy[0] in ideal_hand:
        return True
    return False


def play_game():
    last_turn = starting_hand()
    turns_taken = 1
    while True:
        next_turn = turn(last_turn[0], last_turn[1], last_turn[2])
        last_turn = next_turn
        if has_won(next_turn[0], next_turn[2]) is True:
            break
        turns_taken += 1
    return turns_taken


def find_average(iterations):
    turn_taken_list = []
    for _ in range(iterations):
        turn_taken_list.append(play_game())
    print(sum(turn_taken_list)/len(turn_taken_list))


find_average(10000)
