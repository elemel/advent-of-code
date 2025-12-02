import sys


def is_repeated(s):
	i = len(s)
	return any(s[:j] * (i // j) == s for j in range(1, i // 2 + 1))


def solve_part_1(lines):
	result = 0

	for line in lines:
		for range_str in line.split(","):
			start_str, end_str = range_str.split("-")

			start = int(start_str)
			end = int(end_str)

			for i in range(start, end + 1):
				i_str = str(i)

				if i_str[:len(i_str) // 2] == i_str[len(i_str) // 2:]:
					result += i

	return result


def solve_part_2(lines):
	result = 0

	for line in lines:
		for range_str in line.split(","):
			start_str, end_str = range_str.split("-")

			start = int(start_str)
			end = int(end_str)

			for i in range(start, end + 1):
				i_str = str(i)

				if is_repeated(i_str):
					result += i

	return result


if __name__ == "__main__":
	lines = list(sys.stdin)
	print(solve_part_1(lines))
	print(solve_part_2(lines))
