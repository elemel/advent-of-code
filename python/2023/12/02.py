import sys
from math import prod

CUBES = dict(red=12, green=13, blue=14)


def parse_round(s):
	result = {}

	for part in s.split(","):
		count_str, color = part.split()
		result[color] = int(count_str)

	return result


def parse_game(line):
	id_str, rounds_str = line.split(":")
	_, id_str = id_str.split()
	rounds = [parse_round(s) for s in rounds_str.split(";")]
	return int(id_str), rounds


def is_possible_round(round_):
	return all(count <= CUBES[color] for color, count in round_.items())


def is_possible_game(rounds):
	return all(is_possible_round(r) for r in rounds)


def get_power(game):
	max_counts = {}

	for round_ in game:
		for color, count in round_.items():
			max_counts[color] = max(count, max_counts.get(color, 0))

	return prod(max_counts.values())


def main():
	games = [parse_game(line) for line in sys.stdin]
	print(sum(id_ for id_, rounds in games if is_possible_game(rounds)))
	print(sum(get_power(game) for id_, game in games))


if __name__ == "__main__":
	main()
