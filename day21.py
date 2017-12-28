"""
Solution for Day 21 of Advent of Code 2017.

Problem: Fractal Art

Part 1: After following the strange enhancement rules in the input to
"grow" the image, how many pixels are on after 5 iterations?

Part 2: How many pixels are on after 18 iterations?
"""
import numpy as np

def array_to_tuple(array):
    return tuple(map(tuple, array))

def parse_rules(name):
    rules = {}
    with open(name) as f:
        for line in f:
            _input, _, output = line.split()
            in_rows = tuple(map(tuple, tuple(_input.split("/"))))
            out_rows = np.array(tuple(map(tuple, tuple(output.split("/")))))
            rules[in_rows] = out_rows
    return rules

def deduce_missing_rules(rules):
    deduced_rules = {}
    for r in rules:
        r_array = np.array(r)
        generate_grid_elements(r_array, rules, deduced_rules, r)

        # for 3 x 3 sq's, flip the grid and rotate 4 times again to
        # generate the other 4 elements in the group
        if r_array.shape == (3, 3):
            flipped_r = np.fliplr(r_array)
            generate_grid_elements(flipped_r, rules, deduced_rules, r)

    # merge the given rules and deduced rules dicts before returning
    return {**rules, **deduced_rules}

def generate_grid_elements(r_array, given_rules, deduced_rules, current_rule):
    """
    r_array = rule grid represented in a numpy array.
    current_rule = the current rule represented as tuple (so that it can be
    used as key for dict) currently in consideration.
    """
    for time in range(1, 5):
        rotated_r = np.rot90(r_array, k=time, axes=(1, 0))
        tuple_r = tuple(map(tuple, rotated_r))
        if tuple_r in given_rules:
            continue
        else:
            deduced_rules[tuple_r] = given_rules[current_rule]

def enhance_grid(grid, rules, iterations):
    for i in range(iterations):
        if len(grid) == 3: # cheap short-circuit for first iteration...
            grid = rules[grid]
        else:
            grid = get_new_grid(grid, rules)
    return grid

def get_new_grid(grid, rules):
    size = grid.shape[0]
    step = 2 if size % 2 == 0 else 3

    new_rows = []
    for row in range(0, size, step):
        new_cols = []
        for col in range(0, size, step):
            # prepare the small replacement grids in horizontal direction
            new_cols.append(rules[array_to_tuple(grid[row:row + step, col:col + step])])
        # merge the small replacement grids to form the rows of the new grid
        new_rows.append(np.concatenate(new_cols, axis=1))
    # merge the new rows to complete the new grid
    return np.concatenate(new_rows, axis=0)


if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    rules = parse_rules("day21_input.txt")
    rules = deduce_missing_rules(rules)
    starting_grid = ((".", "#", "."), (".", ".", "#"), ("#", "#", "#"))
    enhanced_grid = enhance_grid(starting_grid, rules, 5)
    u, counts = np.unique(enhanced_grid, return_counts=True)
    # not as neat as previous solutions... but basically read the number
    # immediately below the "#" to get the answer
    print(u)
    print(counts)
    print()

    print("=" * 15, "Part 2", "=" * 15)
    enhanced_grid_2 = enhance_grid(starting_grid, rules, 18)
    u, counts = np.unique(enhanced_grid_2, return_counts=True)
    print(u)
    print(counts)
    # print()
