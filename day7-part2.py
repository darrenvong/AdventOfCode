from collections import Counter

class ProgNode:
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children

def build_tree():
    weights_w_children = {}
    with open("day7_input.txt") as f:
        for line in f:
            row = line.split()
            try:
                arrow_idx = row.index("->")
                children = [c.strip(",") for c in row[arrow_idx + 1:]]
                weights_w_children[row[0]] = int(row[1].strip("()")), children
            except ValueError:
                weights_w_children[row[0]] = int(row[1].strip("()")), []

    # Print imbalance node
    for prog, (weight, prog_children) in weights_w_children.items():
        # do something with prog_children
        c_weights = map(lambda x: weights_w_children[x][0], prog_children)
        c_weight_count = Counter(c_weights)
        if len(c_weight_count) > 1:
            print(f"**{prog}** has imbalanced children!")
            for ws in c_weight_count:
                print(ws)
