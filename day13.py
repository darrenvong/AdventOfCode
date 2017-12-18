"""
Solution for Day 13 of Advent of Code 2017.

Problem: Packet Scanners

Part 1: What is the severity of the trip? Severity defined by the sum of
the layer the packet is being caught multiplied by the layer's range

Part 2: What's the minimum delay such that the packet won't get caught?
"""
from itertools import count

def get_scanner_pos(ps, depth, firewall):
    return ps % ((firewall[depth] - 1) * 2) if depth in firewall else -1

def calculate_severity(firewall):
    total_picosecs = max(firewall) + 1
    severity = 0

    for ps in range(total_picosecs):
        # scanner is there as packet moves in
        if get_scanner_pos(ps, ps, firewall) == 0:
            # so packet caught which adds to severity score
            severity += ps * firewall[ps]

    return severity

def get_min_delay(firewall):
    total_picosecs = max(firewall) + 1

    for delay in count(start=1):
        try:
            for ps in range(delay, total_picosecs + delay):
                # packet is caught
                if get_scanner_pos(ps, ps - delay, firewall) == 0:
                    raise StopIteration
            return delay
        except StopIteration:
            continue

if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    firewall = {}
    with open("day13_input.txt") as f:
        for line in f:
            depth, _range = line.split(": ")
            firewall[int(depth)] = int(_range)
    print(f"The severity score is {calculate_severity(firewall)}")
    print()

    print("=" * 15, "Part 2", "=" * 15)
    print(f"The min picoseconds to delay w/o getting caught is {get_min_delay(firewall)}")
