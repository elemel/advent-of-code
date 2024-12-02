from sys import stdin


def parse_pair(line):
    left, right = map(int, line.split())
    return left, right


def main():
    pairs = list(map(parse_pair, stdin))
    left_list, right_list = zip(*pairs)
    print(
        sum(
            abs(left - right)
            for left, right in zip(sorted(left_list), sorted(right_list))
        )
    )
    print(sum(left * right_list.count(left) for left in left_list))


if __name__ == "__main__":
    main()
