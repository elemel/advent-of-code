from sys import stdin
from functools import cache


@cache
def is_even_stone(stone):
    return len(str(stone)) % 2 == 0


@cache
def split_stone(stone):
    stone_str = str(stone)
    half_len = len(stone_str) // 2

    left = int(stone_str[:half_len])
    right = int(stone_str[half_len:])

    return left, right


@cache
def blink(stone, count):
    if count <= 0:
        return 1

    if stone == 0:
        return blink(1, count - 1)

    if is_even_stone(stone):
        return sum(blink(half_stone, count - 1) for half_stone in split_stone(stone))

    return blink(stone * 2024, count - 1)


def main():
    stones = list(map(int, stdin.read().split()))

    for count in [25, 75]:
        print(sum(blink(stone, count) for stone in stones))


if __name__ == "__main__":
    main()
