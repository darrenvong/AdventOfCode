"""
Solution for Day 18 of Advent of Code 2017.

Problem: Duet

Part 2: How many times have program 1 (the second program) sent something?
"""
from collections import defaultdict, deque
from day18 import is_digit, update_current

def get_num_values_sent(instructions, prog_num, send_queue, rcved_queue, states):
    registers = defaultdict(int, {"p": prog_num})
    num_instructions = len(instructions)
    if prog_num == 1:
        send_count = 0
    current = 0

    while current < num_instructions:
        cmd, args = instructions[current].split(maxsplit=1)
        if cmd != "snd" and cmd != "rcv":
            x, y = args.split()

        if cmd == "snd":
            if prog_num == 1:
                send_count += 1
            send_queue.append((int(args) if is_digit(args) else registers[args]))
        elif cmd == "set":
            registers[x] = int(y) if is_digit(y) else registers[y]
        elif cmd == "add":
            registers[x] += int(y) if is_digit(y) else registers[y]
        elif cmd == "mul":
            registers[x] *= int(y) if is_digit(y) else registers[y]
        elif cmd == "mod":
            registers[x] %= int(y) if is_digit(y) else registers[y]
        elif cmd == "jgz":
            if x.isalpha():
                if registers[x] > 0:
                    current = update_current(y, current, registers)
                    continue
            elif int(x) > 0:
                current = update_current(y, current, registers)
                continue
        elif cmd == "rcv":
            if rcved_queue:
                registers[args] = rcved_queue.popleft()
            else:
                # other prog has finished and so won't get anymore value, so this has
                # to terminate too
                if states[1-prog_num] == "done":
                    break
                # not sending anything and other prog is waiting - deadlock
                elif not send_queue and states[1-prog_num] == "waiting":
                    break
                else:
                    # so rcv command can be tried again when returning to this function
                    current -= 1
                    yield "waiting"
        current += 1

    if prog_num == 1:
        print(f"{send_count} messages sent by program 1")
    yield "done"

if __name__ == '__main__':
    print("=" * 15, "Part 2", "=" * 15)
    with open("day18_input.txt") as f:
        instructions = [line.strip() for line in f]
    states = ["standby", "standby"]
    prog0_queue = deque([])
    prog1_queue = deque([])
    prog0 = get_num_values_sent(instructions, 0, prog1_queue, prog0_queue, states)
    prog1 = get_num_values_sent(instructions, 1, prog0_queue, prog1_queue, states)
    try:
        while True:
            states[0] = next(prog0)
            states[1] = next(prog1)
    except StopIteration:
        pass # only there to stop the program crashing with an expected exception
