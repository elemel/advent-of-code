from sys import stdin
from functools import cmp_to_key


def parse_rule(line):
    a, b = map(int, line.split("|"))
    return a, b


def parse_update(line):
    return list(map(int, line.split(",")))


def main():
    rules_str, updates_str = stdin.read().split("\n\n")

    rules = set(map(parse_rule, rules_str.splitlines()))
    updates = list(map(parse_update, updates_str.splitlines()))

    def cmp(a, b):
        return int((b, a) in rules) - int((a, b) in rules)

    answers = [0, 0]

    for update in updates:
        fixed_update = sorted(update, key=cmp_to_key(cmp))
        incorrect = fixed_update != update
        answers[incorrect] += fixed_update[len(fixed_update) // 2]

    for answer in answers:
        print(answer)


if __name__ == "__main__":
    main()
