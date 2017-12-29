"""
Solution for Day 23 of Advent of Code 2017.

Problem: Coprocessor Conflagration

Probably the toughest challenge to date for me, and the first where I felt
I didn't "complete" it without masses of help from reading hints on Reddit, which
helped me (very slowly) learnt how the assembly program is trying to count the
number of composites between b and c for part 2!
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

def basic_optimise():
    B = 79 * 100 + 100000
    c = B + 17000
    h = 0

    for b in range(B, c + 1, 17):
        f = 1
        for d in range(2, B):
            # eliminated e's loop as it's unnecessarily checking whether
            # either d or e is a multiple of B
            if b % d == 0:
                f = 0
                break
        if f == 0:
            h += 1
    return h

def is_prime(n):
    # from https://en.wikipedia.org/wiki/Primality_test
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def super_optimised():
    B = 79 * 100 + 100000
    c = B + 17000
    h = 0
    for b in range(B, c + 1, 17):
        if not is_prime(b):
            h += 1
    return h

if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    with open("day23_input.txt") as f:
        instructions = [line.split() for line in f]
    print(f"The `mul` instruction gets run {get_num_times_mul_invoked(instructions)} times.")

    print("=" * 15, "Part 2", "=" * 15)
    print(f"h = {super_optimised()}")
