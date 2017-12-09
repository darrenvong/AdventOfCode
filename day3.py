"""
Solution for Day 3 of Advent of Code 2017.

Problem: Spiral Memory

Part 1: Find the Manhattan distance between the location of my input data and the square `1`
(the origin). Each value in the square is allocated in a spiral pattern.

Part 2: Find the first value in memory which will be larger than my input data. In this part,
the value for each square is obtained by taking summing the value from adjacent squares,
including diagonals.
"""
from collections import defaultdict

def get_manhattan_distance(num_input=277678):
    for i, (x, y) in enumerate(get_next_square_coordinate(step_limit=527), start=1):
        if i == num_input:
            return abs(x) + abs(y)

def get_first_value_larger_than_input(num_input=277678):
    grid = defaultdict(int)
    grid[0, 0] = 1 # first sq starts with value of 1

    for x, y in get_next_square_coordinate(step_limit=527):
        if (x, y) != (0, 0):
            grid[x, y] = (grid[x + 1, y] + grid[x + 1, y + 1] + grid[x, y + 1] +
                          grid[x - 1, y + 1] + grid[x - 1, y] + grid[x - 1, y - 1] +
                          grid[x, y - 1] + grid[x + 1, y - 1])

        if grid[x, y] >= num_input:
            return grid[x, y]

def get_next_square_coordinate(step_limit=3):
    """Pattern seems to be that it goes x number of steps right/up, then
    x + 1 steps left/down, then x + 2 steps right up and so on."""
    curX, curY = (0, 0)
    step = 1
    direction = 1 # 1 for right/up, -1 for left/down
    yield (curX, curY) # first square
    while step <= step_limit:
        # spiralling left/right
        for _ in range(step):
            curX += direction
            yield (curX, curY)

        # spiralling up/down
        for _ in range(step):
            curY += direction
            yield (curX, curY)

        step += 1
        direction *= -1


if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    print(f"The Manhattan distance between my input data and 1 is {get_manhattan_distance()}")
    print()

    print("=" * 15, "Part 2", "=" * 15)
    print(f"The first value written that's larger than my input "
          f"is {get_first_value_larger_than_input()}")
