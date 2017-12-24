"""
Solution for Day 16 of Advent of Code 2017.

Problem: Permutation Promenade

Part 1: Given the dance moves, what order are the programs standing in after one dance?

Part 2: What order are the programs standing in after one billion dances?

Main breakthrogh is the realisation that after x dances, the initial order is obtainable
again (i.e. there's a cycle)
"""
from itertools import count

def get_prog_order_after_dance(moves, progs):
    for move in moves:
        if "s" in move:
            spin_size = int(move[1:])
            progs[:-spin_size], progs[-spin_size:] = progs[-spin_size:], progs[:-spin_size]
        elif "x" in move:
            first, second = tuple(map(int, move[1:].split("/")))
            progs[first], progs[second] = progs[int(second)], progs[int(first)]
        elif "p" in move:
            first, second = tuple(map(progs.index, move[1:].split("/")))
            progs[first], progs[second] = progs[second], progs[first]
    return "".join(progs)

def get_cycle(moves, progs):
    seen = ["".join(progs)]
    for _ in count(start=1):
        prog_list = get_prog_order_after_dance(moves, progs)
        if prog_list in seen:
            return seen
        else:
            seen.append(prog_list)

if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    with open("day16_input.txt") as f:
        moves = f.read().strip().split(",")
    progs = list("abcdefghijklmnop")
    print(f"The program's order after the dance is {get_prog_order_after_dance(moves, progs)}")
    print()

    print("=" * 15, "Part 2", "=" * 15)
    progs = list("abcdefghijklmnop")
    cycle = get_cycle(moves, progs)
    print(f"The programs order after one billion dances is {cycle[1000000000 % len(cycle)]}")
