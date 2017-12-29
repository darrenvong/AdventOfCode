"""
Solution for Day 24 of Advent of Code 2017.

Problem: Electromagnetic Moat

Strength of the bridge defined by the sum of the pin value of the components
used to build the bridge.

Part 1: What is the strength of the strongest bridge?

Part 2: What is the strength of the strongest & longest bridge?

Another toughie for me. The biggest breakthrough came about when I woke up
to the idea of building/storing the bridge as a trie, as the data structure takes
advantage of large common prefixes between valid bridges.
"""
from collections import deque

class TrieNode:
    def __init__(self, val, level, children):
        self.val = val # int
        self.level = level # int
        self.children = children # dict<tuple, TrieNode>

def generate_bridge(components, trie: TrieNode, l_prev=0, r_prev=0):
    for l_port, r_port in components:
        if trie.val == 0:
            if l_port == 0:
                _next = TrieNode(sum((l_port, r_port)), trie.level + 1, {})
                trie.children[l_port, r_port] = _next
                generate_bridge(components - {(l_port, r_port)}, _next, l_port, r_port)
        else:
            # l_prev, r_prev = trie.val
            if l_port == r_prev or r_port == r_prev:
                _next = TrieNode(sum((l_port, r_port), trie.val), trie.level + 1, {})
                if l_port == r_prev:
                    trie.children[l_port, r_port] = _next
                    generate_bridge(components - {(l_port, r_port)}, _next, l_port, r_port)
                else:
                    trie.children[r_port, l_port] = _next
                    generate_bridge(components - {(l_port, r_port)}, _next, r_port, l_port)

def breadth_first_search(root_trie: TrieNode):
    nodes_to_visit = deque([root_trie])
    visited = []

    while nodes_to_visit:
        cur_node = nodes_to_visit.popleft()
        visited.append(cur_node)
        for c, c_node in cur_node.children.items():
            nodes_to_visit.append(c_node)
    return visited


def get_strongest_bridge(trie_nodes):
    return max(trie_nodes, key=lambda n: n.val).val

def get_strongest_longest_bridge(trie_nodes):
    return sorted(sorted(trie_nodes, key=lambda n: n.val), key=lambda n: n.level)[-1]

def calculate_longest_strength(trie):
    if not trie.children:
        return sum(trie.val)
    else:
        total = 0
        for c, c_node in trie.children.items():
            total += calculate_longest_strength(c_node)
        return total

if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    with open("day24_input.txt") as f:
        components = {tuple(map(int, line.strip().split("/"))) for line in f}
    root_trie = TrieNode(0, 0, {})
    generate_bridge(components, root_trie)
    trie_nodes = breadth_first_search(root_trie)
    strongest = get_strongest_bridge(trie_nodes)
    print(f"The strength of the strongest bridge is {strongest}")
    print()

    print("=" * 15, "Part 2", "=" * 15)
    strongest_long = get_strongest_longest_bridge(trie_nodes)
    print(f"The longest strongest bridge has strength {strongest_long.val}")
