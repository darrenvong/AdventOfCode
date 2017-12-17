"""
Solution for Day 9 of Advent of Code 2017.

Problem: Stream Processing

Part 1: What is the total score of all groups in the stream? Each group
has a score corresponding to the level in which the group is in (i.e. a
sub-sub-group has a score of 3 since it is 3 levels in - the outermost
group counts as level 1).

Part 2: Excluding the start and end delimiting chars, the "!" char and any
chars canceled by "!", how many non-canceled garbage characters are in
the stream?
"""

def get_solutions(stream):
    garbage_char_count = 0
    is_garbage = False
    skip_next = False
    group_level = 0
    score = 0

    for char in stream:
        if is_garbage:
            if skip_next:
                skip_next = False
                continue
            elif char == "!":
                skip_next = True
            elif char == ">":
                is_garbage = False
            else:
                garbage_char_count += 1
        elif char == "<":
            is_garbage = True
        elif char == "{":
            group_level += 1
        elif char == "}":
            score += group_level
            group_level -= 1

    return score, garbage_char_count


if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    with open("day9_input.txt") as f:
        stream = f.read().strip()
    score, garbage_char_count = get_solutions(stream)
    print(f"The total score is {score}")
    print()

    print("=" * 15, "Part 2", "=" * 15)
    # print()
    print(f"There are {garbage_char_count} of non-canceled garbage chars")
