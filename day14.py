"""
Solution for Day 14 of Advent of Code 2017.

Problem: Disk Defragmentation

Part 1: Converting the given input into its binary Knot Hash equivalent, how many
squares (1s) are being used?

Part 2: How many contiguous (not counting diagonal neighbours) regions are there?
"""
from collections import Counter

from day10 import convert_input_to_ascii_code, get_knot_hash, run_knot_hash

def get_num_squares_used(_input):
    rows = map(convert_input_to_ascii_code, (f"{_input}-{i}" for i in range(128)))
    knot_hashes = map(get_knot_hash, map(lambda x: run_knot_hash(x, rounds=64), rows))
    bin_knot_hashes = []
    for i, kh_row in enumerate(knot_hashes):
        bin_knot_hashes.append([])
        for digit in kh_row:
            bin_knot_hashes[i].append(hex_to_bin(digit))
        bin_knot_hashes[i] = "".join(bin_knot_hashes[i])

    return sum(map(lambda x: Counter(x)["1"], bin_knot_hashes)), bin_knot_hashes

def hex_to_bin(hex_num):
    return "{:04b}".format(int(hex_num, base=16))

def count_regions(bin_knot_hashes):
    seen = set()
    regions_count = 0
    for i in range(128):
        for j in range(128):
            if (i, j) in seen:
                continue
            # square not been seen, so must be the start of a new region
            elif bin_knot_hashes[i][j] == "1":
                regions_count += 1
                check_neighbours(i, j, bin_knot_hashes, seen)

    return regions_count

def check_neighbours(x, y, bin_knot_hashes, seen):
    if (x, y) in seen:
        return
    elif bin_knot_hashes[x][y] == "1":
        seen.add((x, y))

        if x > 0:
            check_neighbours(x - 1, y, bin_knot_hashes, seen)
        if y > 0:
            check_neighbours(x, y - 1, bin_knot_hashes, seen)
        if x < 127:
            check_neighbours(x + 1, y, bin_knot_hashes, seen)
        if y < 127:
            check_neighbours(x, y + 1, bin_knot_hashes, seen)

if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    day_input = "wenycdww"
    num_used, bin_knot_hashes = get_num_squares_used(day_input)
    print(f"{num_used} squares are being used")
    print()

    print("=" * 15, "Part 2", "=" * 15)
    print(f"There are {count_regions(bin_knot_hashes)} regions!")
