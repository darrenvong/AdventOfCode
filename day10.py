"""
Solution for Day 10 of Advent of Code 2017.

Problem: Knot Hash (algorithm)

Part 1: What's the product of the first two numbers in the "marks" list after
running one round of the algorithm?

Part 2: After converting the input into its ASCII value, what's the Knot Hash
of the puzzle input? Knot Hash obtained by running the algorithm 64 times with the
ASCII valued input, converting the resultant "marks" list into a more compact dense
hash by XOR'ing the 256 numbers in blocks of 16 before converting the value of the
blocks to its hex representation.
"""
from functools import reduce

def convert_input_to_ascii_code(_input):
    return list(map(ord, _input)) + [17, 31, 73, 47, 23]

def run_knot_hash(lengths, rounds=1):
    marks = list(range(256))
    len_marks = len(marks)
    cur_pos = 0
    skip_size = 0

    for _ in range(rounds):
        for length in lengths:
            reversed_sub_list = [marks[(cur_pos + i) % len_marks] for i in range(length)][::-1]
            for i, m in enumerate(reversed_sub_list):
                marks[(cur_pos + i) % len_marks] = m
            cur_pos += length + skip_size
            skip_size += 1

    return marks

def get_result(marks):
    return marks[0] * marks[1]

def get_knot_hash(sparse):
    # sparse[i: i + 16] represents each of the 16 blocks in the dense_hash
    dense_hash = [reduce(lambda x, y: x ^ y, sparse[i:i + 16]) for i in range(0, 256, 16)]
    hex_hash = map("{:02x}".format, dense_hash)
    return "".join(hex_hash)


if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    with open("day10_input.txt") as f:
        lengths = map(int, f.read().strip().split(","))
    result = get_result(run_knot_hash(lengths, 1))
    print(f"The result of multiplying the first two number is {result}")
    print()

    print("=" * 15, "Part 2", "=" * 15)
    with open("day10_input.txt") as f:
        lengths = f.read().strip()
    ascii_lengths = convert_input_to_ascii_code(lengths)
    sparse_hash = run_knot_hash(ascii_lengths, rounds=64)
    knot_hash = get_knot_hash(sparse_hash)
    print(f"The knot hash of my puzzle input is {knot_hash}")
