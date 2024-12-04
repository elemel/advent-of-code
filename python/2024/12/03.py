from sys import stdin
import re


def main():
    code = stdin.read()

    answer_1 = 0
    answer_2 = 0

    enabled = True

    for instruction in re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", code):
        match instruction:
            case "do()":
                enabled = True

            case "don't()":
                enabled = False

            case _:
                a, b = re.findall(r"\d+", instruction)
                answer_1 += int(a) * int(b)
                answer_2 += enabled * int(a) * int(b)

    print(answer_1)
    print(answer_2)


if __name__ == "__main__":
    main()
