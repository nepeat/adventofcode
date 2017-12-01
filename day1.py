import os

from collections import defaultdict

def sum_valids(valid_digits: dict):
    total = 0

    for digit, count in valid_digits.items():
        total += int(digit) * count

    return total

def captcha_pt1(password: str):
    valid_digits = defaultdict(lambda: 0)
    password_length = len(password)
    current_pos = 0

    while current_pos < password_length:
        digit_pair_1 = password[current_pos]
        if current_pos + 1 > password_length - 1:
            digit_pair_2 = password[0]
        else:
            digit_pair_2 = password[current_pos + 1]

        if digit_pair_1 == digit_pair_2:
            valid_digits[digit_pair_1] += 1

        current_pos += 1

    return sum_valids(valid_digits)

def captcha_pt2(password: str):
    valid_digits = defaultdict(lambda: 0)
    password_length = len(password)
    half_length = int(len(password) / 2)
    current_pos = 0

    while current_pos < password_length:
        digit_pair_1 = password[current_pos]
        if current_pos + password_length > password_length - 1:
            digit_pair_2 = password[current_pos - half_length]
        else:
            digit_pair_2 = password[current_pos + half_length]

        if digit_pair_1 == digit_pair_2:
            valid_digits[digit_pair_1] += 1

        current_pos += 1

    return sum_valids(valid_digits)

def test(part1_password: str=None, part2_password: str=None):
    PART1_TEST = {
        "1122": 3,
        "1111": 4,
        "1234": 0,
        "91212129": 9
    }

    PART2_TEST = {
        "1212": 6,
        "1221": 0,
        "123425": 4,
        "123123": 12,
        "12131415": 4
    }

    for password, expected in PART1_TEST.items():
        result = captcha_pt1(password)
        if result == expected:
            print(f"1 OK: {result} == {expected}")
        else:
            print(f"1 BAD: {result} != {expected}")

    for password, expected in PART2_TEST.items():
        result = captcha_pt2(password)
        if result == expected:
            print(f"2 OK: {result} == {expected}")
        else:
            print(f"2 BAD: {result} != {expected}")

    if part1_password:
        print("-" * 15)
        print(captcha_pt1(part1_password))

    if part2_password:
        print("-" * 15)
        print(captcha_pt2(part2_password))

if __name__ == "__main__":
    test(os.environ.get("PART1", None), os.environ.get("PART2", None))
