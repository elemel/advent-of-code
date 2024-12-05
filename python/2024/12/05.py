from sys import stdin
from functools import cmp_to_key


def main():
    rules_str, updates_str = stdin.read().split("\n\n")

    rules = {tuple(map(int, l.split("|"))) for l in rules_str.splitlines()}
    updates = [list(map(int, l.split(","))) for l in updates_str.splitlines()]

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
