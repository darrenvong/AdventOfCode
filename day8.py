"""
Solution for Day 8 of Advent of Code 2017.

Problem: I Heard You Like Registers

Part 1: What is the largest value in any register after all instructions
are run?

Part 2: What is the largest value held in any register during the process
of running the instructions?
"""
import re
from collections import defaultdict

def get_highest_register():
    instruction_re = re.compile(r"(\w+)\s(\+|\-)\s(-?\d+)\s(if)\s(\w+)([\w\s<>!=\-]+)")
    registers = defaultdict(int)
    highest = -1
    with open("day8_input.txt") as f:
        for line in f:
            if "inc" in line:
                line = line.replace("inc", "+").strip()
            else:
                line = line.replace("dec", "-").strip()

            pythonic_instruction = instruction_re.sub(
                r"registers['\1'] \2= \3 \4 registers['\5']\6 else 0", line)
            exec(pythonic_instruction)
            highest = max(list(registers.values()) + [highest])

    return max(registers.values()), highest


if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    current_highest, highest = get_highest_register()
    print(f"The largest value in the registers is {current_highest}")

    print("=" * 15, "Part 2", "=" * 15)
    print(f"The highest value held ever is {highest}")
