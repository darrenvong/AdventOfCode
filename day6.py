"""
Solution for Day 6 of Advent of Code 2017.

Problem: Memory Reallocation

Part 1: ??

Part 2: ??
"""
from itertools import count

def get_num_redistribution_cycles():
    with open("day6_input.txt") as f:
        banks = list(map(int, f.read().strip().split("\t")))
    history = []

    while True:
        # finds the memory bank with most blocks
        highest_num_blocks, highest_index = get_highest_num_blocks_and_index(banks)

        redistribute_blocks(banks, highest_num_blocks, highest_index)

        # check if current state has been seen before
        if banks in history:
            # add to history for final time to get total number of steps
            history.append(list(banks))
            # since index starts at 0
            part2 = (len(history) - 1) - history.index(banks)
            return len(history), history, part2
        else:
            # Unseen state, so add to history for checking later
            history.append(list(banks))

def get_highest_num_blocks_and_index(banks):
    highest_num_blocks = -1
    highest_index = -1
    for idx, num_blocks in enumerate(banks):
        if num_blocks > highest_num_blocks:
            highest_num_blocks = num_blocks
            highest_index = idx
    return highest_num_blocks, highest_index

def redistribute_blocks(banks, highest_num_blocks, highest_index):
    len_banks = len(banks)
    # resets the bank with most blocks as all of them are used for redistribution
    banks[highest_index] = 0
    # redistribute the blocks
    inf_counter = count((highest_index + 1) % len(banks))
    for _ in range(highest_num_blocks, 0, -1):
        index = next(inf_counter) % len_banks
        banks[index] += 1


if __name__ == '__main__':
    len_history, history, part2 = get_num_redistribution_cycles()
    print("=" * 15, "Part 1", "=" * 15)
    print(f"{len_history} cycles to be completed before an existing "
          "configuration produced before is seen")
    print()

    print("=" * 15, "Part 2", "=" * 15)
    print(f"Length of cycle for the seen state: {part2}")
