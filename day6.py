"""
Solution for Day 6 of Advent of Code 2017.

Problem: Memory Reallocation

Reallocation works by finding the memory bank with the most blocks,
and all blocks from that memory bank is then redistributed cyclicly,
one block at a time, starting from the next memory bank relative to the one
with the most blocks. If it reaches the last memory bank, it wraps back
around to the first one.

Part 1: How many redistribution cycles must be completed before
a previously seen configuration appears?

Part 2: What's the length of the cycle?
"""
from itertools import count

def get_num_redistribution_cycles():
    with open("day6_input.txt") as f:
        banks = list(map(int, f.read().split()))
    history = []

    while True:
        # finds the memory bank with most blocks
        highest_num_blocks = max(banks)
        highest_index = banks.index(highest_num_blocks)

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
