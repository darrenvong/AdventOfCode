"""
Solution for Day 25 of Advent of Code 2017.

Problem: Halting Problem

Part 1: What's the checksum after completing the given number of steps?
"""
from collections import defaultdict

def get_checksum():
    state = "A"
    steps_required = 12683008
    cursor = 0
    tape = defaultdict(int)

    for _ in range(steps_required):
        if state == "A":
            if tape[cursor] == 0:
                tape[cursor] = 1
                cursor += 1
                state = "B"
            else:
                tape[cursor] = 0
                cursor -= 1
                state = "B"
        elif state == "B":
            if tape[cursor] == 0:
                tape[cursor] = 1
                cursor -= 1
                state = "C"
            else:
                tape[cursor] = 0
                cursor += 1
                state = "E"
        elif state == "C":
            if tape[cursor] == 0:
                tape[cursor] = 1
                cursor += 1
                state = "E"
            else:
                tape[cursor] = 0
                cursor -= 1
                state = "D"
        elif state == "D":
            tape[cursor] = 1
            cursor -= 1
            state = "A"
        elif state == "E":
            state = "A" if tape[cursor] == 0 else "F"
            tape[cursor] = 0
            cursor += 1
        elif state == "F":
            state = "E" if tape[cursor] == 0 else "A"
            tape[cursor] = 1
            cursor += 1

    return sum(tape.values())

if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    print(get_checksum())
    print()

    print("=" * 15, "Part 2", "=" * 15)
    print("Advent of Code completed! Woohoo!")
