from sys import stdin


def parse_card(line):
    head, tail = line.split(":")
    win_nums_str, nums_str = tail.split("|")

    card_num = int(head.split()[1])
    win_nums = {int(s) for s in win_nums_str.split()}
    nums = {int(s) for s in nums_str.split()}

    return card_num, win_nums, nums


def main():
    lines = [*stdin]

    total_point_val = 0
    card_counts = [1] * len(lines)

    for i, line in enumerate(lines):
        card_num, win_nums, nums = parse_card(line)
        assert card_num == i + 1

        match_count = len(nums & win_nums)

        if match_count:
            total_point_val += 2 ** (match_count - 1)

            for j in range(i + 1, i + 1 + match_count):
                card_counts[j] += card_counts[i]

    print(total_point_val)
    print(sum(card_counts))


if __name__ == "__main__":
    main()
