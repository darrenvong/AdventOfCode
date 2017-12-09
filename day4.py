"""
Solution for Day 4 of Advent of Code 2017.

Problem: High-Entropy Passphrases

Part 1: Count the number of valid passphrases. Valid passphrases are those
that contain no duplicate words. Each word is separated by a space

Part 2: Count the number of valid passphrases, and this time, valid passphrases
are defined to be ones where there are no anagrams of each other in each line.

For more of what the above means, check out the examples used to test the
solution functions I've written.
"""
from collections import Counter

def count_num_valid_passphrases_no_repeat():
    num_valid = 0
    with open("day4_input.txt") as f:
        for line in f:
            row = line.strip().split(" ")

            # if row doesn't contain duplicate, then the list would be empty
            # and so it's "falsey", hence if the negation of it is true,
            # then we know that row contains non-duplicate words
            if not list(filter(lambda x: x > 1, Counter(row).values())):
                num_valid += 1
    return num_valid

def count_num_valid_pass_no_anagrams():
    # general strategy: sort each word, then compare for "equality" to
    # see if they are anagrams of each other
    # TO-DO

    def sort_chars(word):
        """sort characters in word in alphabetical order, and return that
        as a string."""
        return "".join(sorted(word))

    num_valid = 0
    with open("day4_input.txt") as f:
        for line in f:
            row = map(sort_chars, line.strip().split(" "))

            if not list(filter(lambda x: x > 1, Counter(row).values())):
                num_valid += 1
    return num_valid


if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    print(f"{count_num_valid_passphrases_no_repeat()} phrases are valid.")
    print()

    print("=" * 15, "Part 2", "=" * 15)
    print(f"{count_num_valid_pass_no_anagrams()} phrases are valid.")
