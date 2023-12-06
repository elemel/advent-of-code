from sys import stdin
from math import prod


def get_distance(bt, t):
	return bt * (t - bt)


def solve(t, d):
	result = 0

	for bt in range(1, t):
		if get_distance(bt, t) > d:
			result += 1

	return result


def main():
	times_str, distances_str = stdin.read().strip().splitlines()

	times = [int(w) for w in times_str.split()[1:]]
	distances = [int(w) for w in distances_str.split()[1:]]

	print(prod(solve(t, d) for t, d in zip(times, distances)))

	t = int(''.join(times_str.split()[1:]))
	d = int(''.join(distances_str.split()[1:]))

	print(solve(t, d))


if __name__ == "__main__":
	main()
