"""
Solution for Day 5 of Advent of Code 2017.

Problem: A Maze of Twisty Trampolines, All Alike

The goal of this puzzle to follow the jump offset instructions given in the list until
my current offset is **outside** the list. After each jump, the offset of that instruction
needs is incremented by 1.

Part 1: How many steps are needed to exit the puzzle?

Part 2: Same as part 1, except if the offset instruction is >= 3, decrement it by 1
instead after following it.
"""

def get_num_steps_to_exit(part=1):
    with open("day5_input.txt") as f:
        offsets = [int(line.strip()) for line in f]

    num_steps = 0
    cur_pos = 0
    old_pos = 0
    while cur_pos < len(offsets):
        old_pos = cur_pos
        # get instruction of current position
        instruction = offsets[cur_pos]
        # follow the instruction
        cur_pos += instruction
        # increment the instruction at the old position
        if part == 1:
            offsets[old_pos] += 1
        elif part == 2:
            offsets[old_pos] = ((offsets[old_pos] - 1) if instruction >= 3
                                else (offsets[old_pos] + 1))
        # increase step count, now that one step has been taken
        num_steps += 1

    return num_steps

if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    print(f"{get_num_steps_to_exit()} steps are required to reach the exit.")
    print()

    print("=" * 15, "Part 2", "=" * 15)
    print(f"{get_num_steps_to_exit(part=2)} steps are required to reach the exit.")
