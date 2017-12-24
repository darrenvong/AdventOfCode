"""
Solution for Day 17 of Advent of Code 2017.

Problem: Spinlock

Part 1: What's the next number after 2017?

Admittedly cheated a little, but learnt that constantly rotating the deque
to the left by the given steps effectively "pushes" the insertion point to the
end of the list, and so numbers can be appended to the end (more efficient, const time?) rather
than being inserted in the middle of the list (linear time operation)

Part 2: What's the next number after 0, when 50000000 (50 million) has been inserted?
"""
from collections import deque

def get_solution(_input, times=2017, part=1):
    """Returns the next value after `times` has been inserted into the
    circular buffer."""
    buffer = deque([0])
    for i in range(1, times + 1):
        buffer.rotate(-_input)
        buffer.append(i)
    return buffer[0] if part == 1 else buffer[buffer.index(0) + 1]



if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    _input = 345
    # print()
    print(get_solution(_input))

    print("=" * 15, "Part 2", "=" * 15)
    print(get_solution(_input, times=50000000, part=2))
    # print()
