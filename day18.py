"""
Solution for Day 18 of Advent of Code 2017.

Problem: Duet

Part 1: What is the value of last played note when the "rcv" command is called
for the first time?
"""
from collections import defaultdict

def get_first_frequency(instructions):
    registers = defaultdict(int)
    last_played = -1
    num_instructions = len(instructions)
    current = 0

    while current < num_instructions:
        cmd, args = instructions[current].split(maxsplit=1)
        if cmd != "snd" and cmd != "rcv":
            x, y = args.split()

        if cmd == "snd":
            last_played = int(registers[args])
        elif cmd == "set":
            registers[x] = int(y) if is_digit(y) else registers[y]
        elif cmd == "add":
            registers[x] += int(y) if is_digit(y) else registers[y]
        elif cmd == "mul":
            registers[x] *= int(y) if is_digit(y) else registers[y]
        elif cmd == "mod":
            registers[x] %= int(y) if is_digit(y) else registers[y]
        elif cmd == "jgz":
            if x.isalpha():
                if registers[x] > 0:
                    current = update_current(y, current, registers)
                    continue
            elif int(x) > 0:
                current = update_current(y, current, registers)
                continue
        elif cmd == "rcv":
            if registers[args] != 0:
                return last_played
        current += 1

def update_current(val, current, registers):
    try:
        current += int(val)
    except ValueError:
        current += registers[val]
    return current

def is_digit(val):
    return val.isdigit() or val.replace("-", "").isdigit()

if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    with open("day18_input.txt") as f:
        instructions = [line.strip() for line in f]
    print(f"The first recovered frequency is {get_first_frequency(instructions)}")
    print()
