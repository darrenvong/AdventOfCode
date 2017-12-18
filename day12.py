"""
Solution for Day 12 of Advent of Code 2017.

Problem: Digital Plumber

Part 1: How many programs can reach program 0?

Part 2: How many groups are there? A group is a collection of programs that can reach
each other.
"""

def get_num_progs_to_zero(neighbours):
    count = 0
    for prog in neighbours:
        if breadth_first_search(prog, neighbours):
            count += 1

    return count

def breadth_first_search(prog, neighbours, part=1):
    progs_to_visit = []
    visited = []
    progs_to_visit.append(prog)

    while progs_to_visit:
        cur_prog = progs_to_visit.pop(0)
        # check to see if '0' is an immediate neighbour for part 1
        if part == 1 and "0" in neighbours[cur_prog]:
            return True
        visited.append(cur_prog)
        for adjacent in neighbours[cur_prog]:
            if adjacent not in visited and adjacent not in progs_to_visit:
                progs_to_visit.append(adjacent)

    # Part 1: search completed and '0' not found anywhere, so must have no path
    # Part 2: the full group is found from the initial "generator" program
    return False if part == 1 else set(visited)

def get_num_groups(neighbours):
    progs = set(neighbours)
    groups_count = 0

    while progs:
        cur_prog = progs.pop()
        progs = progs - breadth_first_search(cur_prog, neighbours, part=2)
        groups_count += 1

    return groups_count


if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    neighbours = {}
    with open("day12_input.txt") as f:
        for line in f:
            line = line.split()
            arrow_idx = line.index("<->")
            neighbours[line[0]] = [n.strip(",") for n in line[arrow_idx + 1:]]
    print(f"{get_num_progs_to_zero(neighbours)} programs contained program ID 0")
    print()

    print("=" * 15, "Part 2", "=" * 15)
    print(f"There are {get_num_groups(neighbours)} groups")
