"""
Solution for Day 22 of Advent of Code 2017.

Problem: Sporifica Virus

Part 1: Given that the virus infects a node when it's clean, and cleans it when
it's infected, starting from the centre of the map, how many bursts out of 10000
from the virus caused an infection?

Part 2: With the modified logic (see http://adventofcode.com/2017/day/22 for full detail...),
How many bursts out of 10000000 from the virus caused an infection?
"""
from collections import defaultdict

def num_infectious_bursts(name, iterations, part):
    with open(name) as f:
        grid = defaultdict(int, {complex(i, j): int(col == "#") for j, row in enumerate(f)
                                 for i, col in enumerate(row.strip())})

    pos = complex(len(grid) ** 0.5 // 2, len(grid) ** 0.5 // 2) # starts at centre
    direction = 0 - 1j
    count = 0

    for _ in range(iterations):
        if grid[pos] == 1: # infected
            direction *= (0 + 1j) # turns right
            grid[pos] = 0 if part == 1 else 3
        elif grid[pos] == 2: # weakened
            grid[pos] = 1
            if part == 2:
                count += 1
        elif grid[pos] == 3: # flagged
            direction *= -1
            grid[pos] = 0
        else: # clean
            direction /= (0 + 1j) # turns left
            grid[pos] = 1 if part == 1 else 2
            if part == 1:
                count += 1
        # move in direction
        pos += direction

    return count


if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    print(f"{num_infectious_bursts('day22_input.txt', 10000, part=1)} bursts caused an infection")
    print()

    print("=" * 15, "Part 2", "=" * 15)
    print(f"{num_infectious_bursts('day22_input.txt', 10000000, part=2)} "
          "bursts caused an infection")
