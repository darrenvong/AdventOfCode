"""
Solution for Day 15 of Advent of Code 2017.

Problem: Dueling Generators

Part 1: In 40 million iterations, how many pairs of number from the two generators
have matching lower 16-bits?

Part 2: Ditto, but only look at 5 million iterations. Generator changed such that
generator A only generates multiples of 4 and B generates only multiples of 8.
"""
def generate(init, factor, multiple=None):
    result = -1
    divisor = 2147483647
    while True:
        if result == -1:
            result = (init * factor) % divisor
        else:
            result = (result * factor) % divisor

        if multiple is None:
            yield result
        elif result % multiple == 0:
            yield result

def count_matching_lower_half(generator_a, generator_b, rounds=40000000):
    count = 0
    for _ in range(rounds):
        next_a = next(generator_a)
        next_b = next(generator_b)
        filter_mask = 65535 # 2^16 - 1
        if (next_a & filter_mask) - (next_b & filter_mask) == 0:
            count += 1
    return count

if __name__ == '__main__':
    a, b = 116, 299
    generator_a, generator_b = generate(a, 16807), generate(b, 48271)
    print("=" * 15, "Part 1", "=" * 15)
    print(f"There are {count_matching_lower_half(generator_a, generator_b)} pairs "
          "with matching lower 16-bits")
    print()

    print("=" * 15, "Part 2", "=" * 15)
    new_gen_a, new_gen_b = generate(a, 16807, 4), generate(b, 48271, 8)
    print(f"There are now {count_matching_lower_half(new_gen_a, new_gen_b, rounds=5000000)} pairs "
          "with matching lower 16-bits using the new generators")
