from sys import stdin
from collections import Counter


LABELS = "23456789TJQKA"


def parse_label(c):
    return LABELS.index(c) + 2


def parse_hand(s):
    labels = [parse_label(c) for c in s]
    counter = Counter(labels)
    counts = sorted(counter.values(), reverse=True)
    return counts, labels


def parse_hand_and_bid(line):
    hand_str, bid_str = line.split()
    return parse_hand(hand_str), int(bid_str)


def generate_joker_hands(s):
    for target in LABELS:
        if target != "J":
            yield s.replace("J", target)


def parse_hand_and_bid_with_jokers(line):
    hand_str, bid_str = line.split()
    counts, labels = max(parse_hand(s) for s in generate_joker_hands(hand_str))

    labels = [parse_label(c) for c in hand_str]
    labels = [1 if l == 11 else l for l in labels]
    print(labels)
    return (counts, labels), int(bid_str)


def main():
    lines = list(stdin)

    hands_and_bids = [parse_hand_and_bid(line) for line in lines]
    hands_and_bids.sort()

    print(sum(r * b for r, (h, b) in enumerate(hands_and_bids, start=1)))

    hands_and_bids_with_jokers = [
        parse_hand_and_bid_with_jokers(line) for line in lines
    ]
    hands_and_bids_with_jokers.sort()

    print(sum(r * b for r, (h, b) in enumerate(hands_and_bids_with_jokers, start=1)))


if __name__ == "__main__":
    main()
