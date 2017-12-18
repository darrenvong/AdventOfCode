"""
Solution for Day 11 of Advent of Code 2017.

Problem: Hex Ed

 nw (0, 1)
(-1,\  n / (1, 0)
 1)  +--+ ne
    /    \
  -+(0, 0)+-
    \    /
  sw +--+ se (1, -1)
(-1,/ s  \
 0) (0, -1)

Part 1: Given the input steps taken on a hex grid, what is the shortest distance
required to reach the child process from where it started (assume at "origin")?

Part 2: What's the furthest number of steps it ever got from the origin?

http://keekerdc.com/2011/03/hexagon-grids-coordinate-systems-and-distance-calculations/
has helped a lot with a detailed discussion on how to implement a hex grid in 3D. In
particular, since x + y + z = 0, z can be omitted to produce the axial coordinate system.
"""

def get_solutions():
    x, y = (0, 0)
    history = []
    with open("day11_input.txt") as f:
        path = f.read().strip().split(",")

    for move in path:
        if move == "n":
            y += 1
        elif move == "ne":
            x += 1
        elif move == "se":
            x += 1
            y -= 1
        elif move == "s":
            y -= 1
        elif move == "sw":
            x -= 1
        elif move == "nw":
            x -= 1
            y += 1
        history.append((x, y))

    # part 2
    furthest = max(map(lambda p: (abs(p[0]) + abs(p[1]) + abs(p[0] + p[1])) // 2, history))
    return (abs(x) + abs(y) + abs(x + y)) // 2, furthest

if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    distance, furthest = get_solutions()
    print(f"The fewest number of steps required to reach the child process is {distance}")
    print()

    print("=" * 15, "Part 2", "=" * 15)
    print(f"The furthest the process ever got is {furthest}")
