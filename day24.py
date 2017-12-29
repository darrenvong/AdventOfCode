"""
Solution for Day 24 of Advent of Code 2017.

Problem: Electromagnetic Moat

Strength of the bridge defined by the sum of the pin value of the components
used to build the bridge.

Part 1: What is the strength of the strongest bridge?

Part 2: What is the strength of the strongest & longest bridge?

Another toughie for me. The biggest breakthrough came about when I woke up
to the idea of building/storing the bridge in a pseudo-trie (since my final
optimisation ended up removing direct links between trie nodes), as the data structure
takes advantage of large common prefixes between valid bridges.
"""
from collections import deque

class TrieNode:
    def __init__(self, val, level):
        self.val = val # int
        self.level = level # int

def generate_bridge(components, trie: TrieNode, trie_nodes, prev_unused=0):
    for l_port, r_port in components:
        if trie.val == 0:
            if l_port == 0:
                _next = TrieNode(sum((l_port, r_port)), trie.level + 1)
                trie_nodes.append(_next)
                generate_bridge(components - {(l_port, r_port)}, _next, trie_nodes, r_port)
        else:
            if l_port == prev_unused or r_port == prev_unused:
                _next = TrieNode(sum((l_port, r_port), trie.val), trie.level + 1)
                trie_nodes.append(_next)
                if l_port == prev_unused:
                    generate_bridge(components - {(l_port, r_port)}, _next, trie_nodes, r_port)
                else:
                    generate_bridge(components - {(l_port, r_port)}, _next, trie_nodes, l_port)

def get_strongest_bridge(trie_nodes):
    return max(trie_nodes, key=lambda n: n.val).val

def get_strongest_longest_bridge(trie_nodes):
    return sorted(sorted(trie_nodes, key=lambda n: n.val), key=lambda n: n.level)[-1]

def calculate_longest_strength(trie):
    if not trie.children:
        return sum(trie.val)
    else:
        total = 0
        for _, c_node in trie.children.items():
            total += calculate_longest_strength(c_node)
        return total

if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    with open("day24_input.txt") as f:
        components = {tuple(map(int, line.strip().split("/"))) for line in f}
    trie_nodes = []
    root_trie = TrieNode(val=0, level=0)
    generate_bridge(components, root_trie, trie_nodes=trie_nodes)
    strongest = get_strongest_bridge(trie_nodes)
    print(f"The strength of the strongest bridge is {strongest}")
    print()

    print("=" * 15, "Part 2", "=" * 15)
    strongest_long = get_strongest_longest_bridge(trie_nodes)
    print(f"The longest strongest bridge has strength {strongest_long.val}")
