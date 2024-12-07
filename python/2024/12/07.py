from sys import stdin
from operator import add, mul


def concat(a, b):
    return int(str(a) + str(b))


def parse_equation(line):
    test_value_str, numbers_str = line.split(":")
    return int(test_value_str), list(map(int, numbers_str.split()))


def is_valid_equation_rec(result, numbers, ops, total, i):
    if i >= len(numbers):
        return result == total

    return any(is_valid_equation_rec(
        result, numbers, ops, op(total, numbers[i]), i + 1) for op in ops)


def is_valid_equation(result, numbers, ops):
    return is_valid_equation_rec(result, numbers, ops, numbers[0], 1)


def main():
    equations = list(map(parse_equation, list(stdin)))

    for ops in [[add, mul], [add, mul, concat]]:
        print(
            sum(
                result
                for result, numbers in equations
                if is_valid_equation(result, numbers, ops)
            )
        )


if __name__ == "__main__":
    main()
