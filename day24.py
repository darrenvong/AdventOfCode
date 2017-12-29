"""
Solution for Day 24 of Advent of Code 2017.

Problem: Electromagnetic Moat

Part 1: ??

Part 2: ??
"""

def generate_bridge(components, seen, bridge=None):
    for l_port, r_port in components:
        bridge = bridge or []
        if not bridge: # bridge is empty
            if l_port == 0 or r_port == 0:
                bridge.append((l_port, r_port))
                seen.append((bridge, sum(l + r for l, r in bridge)))
                generate_bridge(components, seen, bridge)
                bridge = []
        elif not ((l_port, r_port) in bridge or (r_port, l_port) in bridge):
            unused_port = bridge[-1][1]
            if l_port == unused_port:
                new_bridge = bridge + [(l_port, r_port)]
                if new_bridge not in seen:
                    seen.append((new_bridge, sum(l + r for l, r in new_bridge)))
                    generate_bridge(components, seen, new_bridge)
            elif r_port == unused_port:
                new_bridge = bridge + [(r_port, l_port)]
                if new_bridge not in seen:
                    seen.append((new_bridge, sum(l + r for l, r in new_bridge)))
                    generate_bridge(components, seen, new_bridge)
    return seen

def get_strongest_bridge(bridges):
    return max(bridges, key= lambda x: x[1])[1]

if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    with open("day24_input.txt") as f:
        components = [tuple(map(int, line.strip().split("/"))) for line in f]
    all_bridges = generate_bridge(components, [])
    print(f"Strongest bridge has strength {get_strongest_bridge(all_bridges)}")
    print()

    print("=" * 15, "Part 2", "=" * 15)
    # print()
