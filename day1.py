"""
Solution for Day 1 of Advent of Code 2017.

Problem: Inverse Captcha

Part 1: Find the sum of all digits that match the next digit in the list.

Part 2: Find the sum of all digits that match the digit halfway around the
circular list. For example, if the list has length 10, then a digit which
matches another digit 10/2 = 5 steps forward count towards the sum.

For more of what the above means, check out the examples used to test the
solution functions I've written.
"""

def get_captcha_sum(input_str):
    len_str = len(input_str)
    total = 0
    for i in range(len_str):
        if input_str[i] == input_str[(i + 1) % len_str]:
            total += int(input_str[i])
    return total

def get_captcha_sum_compact(input_str):
    len_str = len(input_str)
    return sum([int(input_str[i]) for i in range(len_str)
                if input_str[i] == input_str[(i + 1) % len_str]])


def get_captcha_sum_steps(input_str):
    len_str = len(input_str)
    step = len_str // 2
    total = 0
    for i in range(len_str):
        if input_str[i] == input_str[(i + step) % len_str]:
            total += int(input_str[i])
    return total

if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    print(get_captcha_sum("1121"), get_captcha_sum_compact("1121"))
    print(get_captcha_sum("1234"), get_captcha_sum_compact("1234"))
    print(get_captcha_sum("1122"), get_captcha_sum_compact("1122"))
    print(get_captcha_sum("91212129"), get_captcha_sum_compact("91212129"))
    with open("day1_challenge1_input.txt") as input_f:
        input_string = input_f.read().strip()
        desired_sum = get_captcha_sum(input_string)
        print(f"The answer to part 1 is {desired_sum}", get_captcha_sum_compact(input_string))
    print()

    print("=" * 15, "Part 2", "=" * 15)
    print(get_captcha_sum_steps("1212"))
    print(get_captcha_sum_steps("1221"))
    print(get_captcha_sum_steps("123425"))
    print(get_captcha_sum_steps("123123"))
    print(get_captcha_sum_steps("12131415"))
    with open("day1_challenge1_input.txt") as input_f:
        input_string = input_f.read().strip()
        desired_sum = get_captcha_sum_steps(input_string)
        print(f"The answer to part 2 is {desired_sum}")
