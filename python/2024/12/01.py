from sys import stdin


def parse_pair(line):
    left, right = [int(s) for s in line.split()]
    return left, right


def main():
    pairs = [parse_pair(line) for line in stdin]
    left_list, right_list = zip(*pairs)
    print(sum(abs(l - r) for l, r in zip(sorted(left_list), sorted(right_list))))
    print(sum(l * right_list.count(l) for l in left_list))


if __name__ == "__main__":
    main()
