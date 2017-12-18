"""
Solution for Day 7 of Advent of Code 2017.

Problem: Recursive Circus

Part 1: What's the name of the bottom program?

Part 2: Given that there's only one program with the wrong weight and causes
the program stack to be imbalanced, what should the correct weight of that
faulty program be?
"""
from collections import Counter

def build_nodes(input_file):
    nodes = {}
    with open(input_file) as f:
        for line in f:
            row = line.split()
            try:
                arrow_idx = row.index("->")
                children = [c.strip(",") for c in row[arrow_idx + 1:]]
                nodes[row[0]] = int(row[1].strip("()")), children
            except ValueError:
                nodes[row[0]] = int(row[1].strip("()")), []

    return nodes

def get_name_of_bottom_program(nodes):
    prog_list = set(nodes.keys())
    prog_has_parent = set() # keeps track of whether a program has parent

    for _, (_, children) in nodes.items():
        for child in children:
            prog_has_parent.add(child)

    diff = prog_list - prog_has_parent
    return diff.pop()


def get_branch_weights(root, nodes):
    _, children = nodes[root]
    branch_weights = {c: calculate_node_weight(nodes, c) for c in children}
    return branch_weights

def get_imbalanced_branch(branch_weights):
    """Gets the base node (program) which has an imbalanced branch."""
    weight_counts = Counter(branch_weights.values())
    for prog, weight in branch_weights.items():
        if weight_counts[weight] == 1:
            return prog
    # if it hits this point, all branches must be balanced
    return None

def find_faulty_prog(root, nodes):
    branch_weights = get_branch_weights(root, nodes)
    imb_root_node = get_imbalanced_branch(branch_weights)
    if imb_root_node is None:
        # all branches balanced, so current root must be the culprit
        return root
    else:
        faulty = find_faulty_prog(imb_root_node, nodes)
        return faulty

def find_correct_weight(faulty_prog, root_prog, nodes):
    branch_weights = get_branch_weights(root_prog, nodes)
    weight_counts = Counter(branch_weights.values())
    ws = map(lambda wc: wc[0], sorted(weight_counts.items(), key=lambda wc: wc[1]))
    err_margin = (lambda x, y: x - y)(*ws)
    return nodes[faulty_prog][0] - err_margin

def calculate_node_weight(nodes, cur_node):
    """Variant of depth first search"""
    weight, children = nodes[cur_node]
    # base case - no children
    if not children:
        return weight
    else:
        total = 0
        for c in children:
            total += calculate_node_weight(nodes, c)
        return total + weight

if __name__ == '__main__':
    nodes = build_nodes("day7_input.txt")
    root_prog = get_name_of_bottom_program(nodes)
    print("=" * 15, "Part 1", "=" * 15)
    print(f"The name of the bottom program is {root_prog}")
    print()

    print("=" * 15, "Part 2", "=" * 15)
    faulty_prog = find_faulty_prog(root_prog, nodes)
    print(f"The faulty program: {faulty_prog}. "
          "The correct weight should be "
          f"{find_correct_weight(faulty_prog, root_prog, nodes)}")
