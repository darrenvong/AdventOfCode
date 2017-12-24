"""
Solution for Day 19 of Advent of Code 2017.

Problem: A series of Tubes

Part 1: What's the order of letters that the packet will encounter as it follows the
diagram?

Part 2: How many steps did it take to go from start to finish?
"""
import numpy as np

def get_trail(diagram):
    end = False
    direction = "S"
    visited = []
    trail = []
    # finds where all pipes are, which seems to be the symbol for the starting square...
    xs, ys = np.where(diagram == "|")
    x, y = xs[0], ys[0]

    while not end:
        visited.append((x, y))
        # move and get content of next square
        if direction == "S":
            x += 1
        elif direction == "W":
            y -= 1
        elif direction == "N":
            x -= 1
        elif direction == "E":
            y += 1
        cur_sq = diagram[x, y]

        # junction hit, so work out which dir to switch
        if cur_sq == "+":
            if (x, y - 1) not in visited and diagram[x, y - 1] != " ":
                direction = "W"
            elif (x, y + 1) not in visited and diagram[x, y + 1] != " ":
                direction = "E"
            elif (x - 1, y) not in visited and diagram[x - 1, y] != " ":
                direction = "N"
            elif (x + 1, y) not in visited and diagram[x + 1, y] != " ":
                direction = "S"
        elif cur_sq.isalpha():
            trail.append(cur_sq)
        elif cur_sq == " ":
            end = True
    
    return "".join(trail), len(visited)

if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    with open("day19_input.txt") as f:
        diagram = np.array([list(line.strip("\n")) for line in f])
    trail, num_steps = get_trail(diagram)
    print(f"The letters the packet sees on its path (in order): {trail}")
    print()

    print("=" * 15, "Part 2", "=" * 15)
    print(f"The total numbers of step taken is {num_steps}")
