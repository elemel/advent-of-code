import sys
from math import prod


def solve_part_1(lines):
    number_lines = [[int(s) for s in line.split()] for line in lines[:-1]]
    operator_line = lines[-1].split()
    transposed_number_lines = list(zip(*number_lines))
    result = 0

    for operator, operands in zip(operator_line, transposed_number_lines):
        if operator == "+":
            result += sum(operands)
        elif operator == "*":
            result += prod(operands)
        else:
            raise Exception()

    return result


def solve_part_2(lines):
    width = len(lines[0])
    height = len(lines)
    result = 0
    numbers = []

    for x in reversed(range(width)):
        column = []

        for y in range(height):
            column.append(lines[y][x])

        operator = column.pop()
        number_str = "".join(column).strip()

        if number_str:
            number = int(number_str)
            numbers.append(number)

            if operator == "+":
                result += sum(numbers)
                numbers = []
            elif operator == "*":
                result += prod(numbers)
                numbers = []
            elif operator == " ":
                pass
            else:
                raise Exception()

    return result


def main():
    lines = list(sys.stdin)
    print(solve_part_1(lines))
    print(solve_part_2(lines))


if __name__ == "__main__":
    main()
