import sys


def solve_part_1(lines):
	dial = 50
	count = 0

	for line in lines:
		direction = -1 if line[0] == "L" else 1
		distance = int(line[1:])
		dial += direction * distance

		if dial % 100 == 0:
			count += 1

	return count


def solve_part_2(lines):
	dial = 50
	count = 0

	for line in lines:
		direction = -1 if line[0] == "L" else 1
		distance = int(line[1:])

		for _ in range(distance):
			dial += direction

			if dial % 100 == 0:
				count += 1

	return count


if __name__ == "__main__":
	lines = list(sys.stdin)
	print(solve_part_1(lines))
	print(solve_part_2(lines))
