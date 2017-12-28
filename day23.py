"""
Solution for Day 23 of Advent of Code 2017.

Problem: Coprocessor Conflagration

"""
from collections import defaultdict
from day18 import is_digit

def get_num_times_mul_invoked(instructions):
    registers = defaultdict(int)
    num_instructions = len(instructions)
    current = 0
    get = lambda val: int(val) if is_digit(val) else registers[val]

    count = 0
    while current < num_instructions:
        cmd, x, y = instructions[current]

        if cmd == "set":
            registers[x] = get(y)
        elif cmd == "sub":
            registers[x] -= get(y)
        elif cmd == "mul":
            registers[x] *= get(y)
            count += 1
        elif cmd == "jnz" and get(x) != 0:
            current += get(y)
            continue
        current += 1
    return count

if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    with open("day23_input.txt") as f:
        instructions = [line.split() for line in f]
    print(get_num_times_mul_invoked(instructions))

    print("=" * 15, "Part 2", "=" * 15)
    # print()
