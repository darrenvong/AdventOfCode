"""
Solution for Day 24 of Advent of Code 2017.

Problem: Electromagnetic Moat

Part 1: ??

Part 2: ??
"""
from collections import deque

class TrieNode:
    def __init__(self, val, children):
        self.val = val # int
        self.children = children # dict<tuple, TrieNode>

def generate_bridge(components, trie: TrieNode, l_prev=0, r_prev=0):
    for l_port, r_port in components:
        if trie.val == 0:
            if l_port == 0:
                _next = TrieNode(sum((l_port, r_port)), {})
                trie.children[l_port, r_port] = _next
                generate_bridge(components - {(l_port, r_port)}, _next, l_port, r_port)
        else:
            # l_prev, r_prev = trie.val
            if l_port == r_prev or r_port == r_prev:
                _next = TrieNode(sum((l_port, r_port), trie.val), {})
                if l_port == r_prev:
                    trie.children[l_port, r_port] = _next
                    generate_bridge(components - {(l_port, r_port)}, _next, l_port, r_port)
                else:
                    trie.children[r_port, l_port] = _next
                    generate_bridge(components - {(l_port, r_port)}, _next, r_port, l_port)

def get_strongest_bridge(root_trie: TrieNode):
    # try depth first search and if I'm still stuck then
    # I'll throw the towel in for a bit...
    nodes_to_visit = deque([root_trie])
    visited = set()

    while nodes_to_visit:
        cur_node = nodes_to_visit.popleft()
        visited.add(cur_node)
        for c, c_node in cur_node.children.items():
            nodes_to_visit.append(c_node)
    return max(visited, key=lambda n: n.val).val

def calculate_longest_strength(trie):
    if not trie.children:
        return sum(trie.val)
    else:
        total = 0
        for c, c_node in trie.children.items():
            total += calculate_longest_strength(c_node)
        return total

# def get_strongest_bridge(bridges):
#     return max(bridges, key= lambda x: x[1])[1]

if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    with open("day24_input.txt") as f:
        components = {tuple(map(int, line.strip().split("/"))) for line in f}
    root_trie = TrieNode(0, {})
    generate_bridge(components, root_trie)
    strongest = get_strongest_bridge(root_trie)
    print(f"The strength of the strongest bridge is {strongest}")
    print()

    print("=" * 15, "Part 2", "=" * 15)
    # print()
