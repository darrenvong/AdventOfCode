"""
Solution for Day 15 of Advent of Code 2017.

Problem: Dueling Generators

Part 1: ??

Part 2: ??
"""
def generate(init, factor):
    result = -1
    while True:
        if result == -1:
            result = (init * factor) % 2147483647
        else:
            result = (result * factor) % 2147483647
        yield result

def count_matching_lower_half(generator_a, generator_b, rounds=40000000):
    count = 0
    for _ in range(rounds):
        next_a = "{:032b}".format(next(generator_a))[16:]
        next_b = "{:032b}".format(next(generator_b))[16:]
        if next_a == next_b:
            count += 1
    return count

if __name__ == '__main__':
    a, b = 116, 299
    generator_a, generator_b = generate(a, 16807), generate(b, 48271)
    print("=" * 15, "Part 1", "=" * 15)
    print(count_matching_lower_half(generator_a, generator_b))
    print()

    print("=" * 15, "Part 2", "=" * 15)
    # print()
