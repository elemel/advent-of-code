from sys import stdin
import operator
from math import prod


OPERATORS = {"<": operator.lt, ">": operator.gt}
EMPTY_RANGED_PART = dict(x=range(0), m=range(0), a=range(0), s=range(0))


def parse_rule(s):
    if ":" in s:
        condition_str, workflow_name = s.split(":")

        if "<" in condition_str:
            category, rating_str = condition_str.split("<")
            condition = category, "<", int(rating_str)
        elif ">" in condition_str:
            category, rating_str = condition_str.split(">")
            condition = category, ">", int(rating_str)

        return condition, workflow_name
    else:
        return [], s


def parse_workflow(s):
    name, rules_str = s.split("{")
    rule_strs = rules_str[:-1].split(",")
    rules = [parse_rule(s) for s in rule_strs]
    return name, rules


def parse_part(s):
    part = {}

    for category_rating_str in s[1:-1].split(","):
        category, rating_str = category_rating_str.split("=")
        part[category] = int(rating_str)

    return part


def evaluate(workflows, workflow_name, part):
    if workflow_name == "A":
        return sum(part.values())
    elif workflow_name == "R":
        return 0

    rules = workflows[workflow_name]

    for condition, workflow_name in rules:
        if not condition:
            return evaluate(workflows, workflow_name, part)

        category, operator_str, rating = condition
        operator = OPERATORS[operator_str]

        if operator(part[category], rating):
            return evaluate(workflows, workflow_name, part)


def split_ranged_part(part, condition):
    if not condition:
        return part, EMPTY_RANGED_PART

    category, operator_str, rating = condition

    true_part = part.copy()
    false_part = part.copy()

    if operator_str == "<":
        true_part[category] = range(part[category].start, rating)
        false_part[category] = range(rating, part[category].stop)
    elif operator_str == ">":
        true_part[category] = range(rating + 1, part[category].stop)
        false_part[category] = range(part[category].start, rating + 1)
    else:
        assert False

    return true_part, false_part


def evaluate_ranged_part(workflows, workflow_name, part):
    if workflow_name == "R":
        return 0

    if not all(len(r) for r in part.values()):
        return 0

    if workflow_name == "A":
        return prod(len(r) for r in part.values())

    result = 0
    rules = workflows[workflow_name]

    for condition, workflow_name in rules:
        new_part, part = split_ranged_part(part, condition)
        result += evaluate_ranged_part(workflows, workflow_name, new_part)

    return result


def main():
    workflows_str, parts_str = stdin.read().split("\n\n")
    workflows = dict(
        parse_workflow(line.strip()) for line in workflows_str.splitlines()
    )
    parts = [parse_part(line.strip()) for line in parts_str.splitlines()]

    print(sum(evaluate(workflows, "in", p) for p in parts))

    part_with_ranges = {c: range(1, 4001) for c in "xmas"}
    print(evaluate_ranged_part(workflows, "in", part_with_ranges))


if __name__ == "__main__":
    main()
