"""
Solution for Day 2 of Advent of Code 2017.

Problem: Corruption Checksum

Part 1: Find the sum of the range (i.e. difference between largest and smallest number)
of each row.

Part 2: Find the sum of the quotient from the pair of values on each row where one can evenly
divide the other.

For more of what the above means, check out the examples used to test the
solution functions I've written.
"""
from itertools import combinations

def calculate_checksum_diff():
    total = 0
    with open("day2_input.txt") as input_f:
        for line in input_f:
            line = line.strip()
            row = list(map(int, line.split("\t")))
            total += max(row) - min(row)
    return total

def calculate_checksum_div():
    total = 0
    with open("day2_input.txt") as input_f:
        for line in input_f:
            line = line.strip()
            row = sorted(map(int, line.split("\t")), reverse=True)

            for n1, n2 in combinations(row, 2):
                if n1 % n2 == 0:
                    total += n1 // n2
                    break
    return total


if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    print(f"The checksum total is {calculate_checksum_diff()}")
    print()

    print("=" * 15, "Part 2", "=" * 15)
    print(f"The checksum total is {calculate_checksum_div()}")
