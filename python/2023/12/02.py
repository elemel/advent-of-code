import sys
from math import prod

CUBES = dict(red=12, green=13, blue=14)


def parse_handful(s):
    handful = {}

    for count_color_str in s.split(","):
        count_str, color = count_color_str.split()
        handful[color] = int(count_str)

    return handful


def parse_game(line):
    id_str, handfuls_str = line.split(":")
    _, id_str = id_str.split()
    id_ = int(id_str)

    handfuls = [parse_handful(s) for s in handfuls_str.split(";")]
    return id_, handfuls


def is_possible_handful(handful):
    return all(count <= CUBES[color] for color, count in handful.items())


def is_possible_game(handfuls):
    return all(is_possible_handful(h) for h in handfuls)


def get_power(game):
    max_counts = {}

    for handful in game:
        for color, count in handful.items():
            max_counts[color] = max(count, max_counts.get(color, 0))

    return prod(max_counts.values())


def main():
    games = [parse_game(line) for line in sys.stdin]
    print(sum(id_ for id_, handfuls in games if is_possible_game(handfuls)))
    print(sum(get_power(game) for id_, game in games))


if __name__ == "__main__":
    main()
