"""
Solution for Day 13 of Advent of Code 2017.

Problem: Packet Scanners

Part 1: What is the severity of the trip? Severity defined by the sum of
the layer the packet is being caught multiplied by the layer's range

Part 2: What's the minimum delay such that the packet won't get caught?
"""
from collections import defaultdict
from itertools import count

def calculate_severity():
    states = defaultdict(lambda: {"range": 0, "scanner_pos": -1, "dir": 1})
    with open("day13_input.txt") as f:
        for line in f:
            line = line.split(": ")
            # states stores the tuple (range_of_layer, scanner_pos)
            states[int(line[0])] = {"range": int(line[1]), "scanner_pos": 0, "dir": 1}

    total_picosecs = max(states) + 1
    severity = 0
    packet_pos = -1
    for ps in range(total_picosecs):
        packet_pos += 1

        # scanner is there as packet moves in
        if states[packet_pos]["scanner_pos"] == 0:
            # so packet caught which adds to severity score
            severity += ps * states[ps]["range"]

        # all scanners move by 1
        for depth in states:
            # if moving ahead will move scanner out of range...
            if (states[depth]["scanner_pos"] + states[depth]["dir"] == states[depth]["range"] or
                    states[depth]["scanner_pos"] + states[depth]["dir"] == -1):
                # then reverse dir first before moving it below
                states[depth]["dir"] *= -1

            states[depth]["scanner_pos"] += states[depth]["dir"]

    return severity

if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    print(f"The severity score (if packet moves as fast as it can) is {calculate_severity()}")
    print()

    print("=" * 15, "Part 2", "=" * 15)
    # print()
