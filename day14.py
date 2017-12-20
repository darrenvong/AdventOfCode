"""
Solution for Day 14 of Advent of Code 2017.

Problem: Disk Defragmentation

Part 1: Converting the given input into its binary Knot Hash equivalent, how many
squares (1s) are being used?

Part 2: ??
"""
from collections import Counter

from day10 import convert_input_to_ascii_code, get_knot_hash, run_knot_hash

def get_num_squares_used(_input):
    rows = map(convert_input_to_ascii_code, (f"{_input}-{i}" for i in range(128)))
    knot_hashes = map(get_knot_hash, map(lambda x: run_knot_hash(x, rounds=64), rows))
    bin_knot_hashes = list(map(hex_to_bin, knot_hashes))
    return sum(map(lambda x: Counter(x)["1"], bin_knot_hashes)), bin_knot_hashes

def hex_to_bin(hex_num):
    return "{:04b}".format(int(hex_num, base=16))

if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    day_input = "wenycdww"
    num_used, bin_knot_hashes = get_num_squares_used(day_input)
    print(f"{num_used} squares are being used")
    print()

    print("=" * 15, "Part 2", "=" * 15)
    # print()
