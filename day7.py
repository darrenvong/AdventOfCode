"""
Solution for Day 7 of Advent of Code 2017.

Problem: Recursive Circus

Part 1: What's the name of the bottom program?

Part 2: ??
"""

def get_name_of_bottom_program():
    prog_list = set()
    prog_has_parent = set() # keeps track of whether a program has parent
    with open("day7_input.txt") as f:
        for line in f:
            row = line.split()
            try:
                prog_list.add(row[0])
                arrow_idx = row.index("->")
                for child in row[arrow_idx + 1:]:
                    prog_has_parent.add(child.strip(","))
            except ValueError:
                # this prog has no children, so carry on...
                continue
    diff = prog_list - prog_has_parent
    return diff

if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    print(f"The name of the bottom program is {list(get_name_of_bottom_program())[0]}")
    print()

    print("=" * 15, "Part 2", "=" * 15)
    # print()
