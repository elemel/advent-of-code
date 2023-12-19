from sys import stdin


def print_grid(grid):
	min_x = min(x for x, y in grid)
	min_y = min(y for x, y in grid)

	max_x = max(x for x, y in grid)
	max_y = max(y for x, y in grid)

	for y in range(min_y, max_y + 1):
		print(''.join(grid[x, y] for x in range(min_x, max_x + 1)))


def to_grid_str(grid):
	min_x = min(x for x, y in grid)
	min_y = min(y for x, y in grid)

	max_x = max(x for x, y in grid)
	max_y = max(y for x, y in grid)

	lines = []

	for y in range(min_y, max_y + 1):
		lines.append(''.join(grid[x, y] for x in range(min_x, max_x + 1)))

	return "\n".join(lines)


def tilt_north(grid):
	min_x = min(x for x, y in grid)
	min_y = min(y for x, y in grid)

	max_x = max(x for x, y in grid)
	max_y = max(y for x, y in grid)

	for x in range(min_x, max_x + 1):
		y = min_y

		while y <= max_y:
			if grid[x, y] == "O":
				while grid.get((x, y - 1)) == ".":
					grid[x, y - 1] = "O"
					grid[x, y] = "."

					y -= 1

			y += 1


def tilt_south(grid):
	min_x = min(x for x, y in grid)
	min_y = min(y for x, y in grid)

	max_x = max(x for x, y in grid)
	max_y = max(y for x, y in grid)

	for x in range(min_x, max_x + 1):
		y = max_y

		while y >= min_y:
			if grid[x, y] == "O":
				while grid.get((x, y + 1)) == ".":
					grid[x, y + 1] = "O"
					grid[x, y] = "."

					y += 1

			y -= 1


def tilt_west(grid):
	min_x = min(x for x, y in grid)
	min_y = min(y for x, y in grid)

	max_x = max(x for x, y in grid)
	max_y = max(y for x, y in grid)

	for y in range(min_y, max_y + 1):
		x = min_x

		while x <= max_x:
			if grid[x, y] == "O":
				while grid.get((x - 1, y)) == ".":
					grid[x - 1, y] = "O"
					grid[x, y] = "."

					x -= 1

			x += 1


def tilt_east(grid):
	min_x = min(x for x, y in grid)
	min_y = min(y for x, y in grid)

	max_x = max(x for x, y in grid)
	max_y = max(y for x, y in grid)

	for y in range(min_y, max_y + 1):
		x = max_x

		while x >= min_x:
			if grid[x, y] == "O":
				while grid.get((x + 1, y)) == ".":
					grid[x + 1, y] = "O"
					grid[x, y] = "."

					x += 1

			x -= 1


def get_total_load(grid):
	min_x = min(x for x, y in grid)
	min_y = min(y for x, y in grid)

	max_x = max(x for x, y in grid)
	max_y = max(y for x, y in grid)

	total_load = 0

	for x in range(min_x, max_x + 1):
		load = 0

		for y in range(max_y, min_y - 1, -1):
			load += 1

			if grid[x, y] == "O":
				total_load += load

	return total_load


def solve_part_1(grid):
	grid = grid.copy()
	tilt_north(grid)
	return get_total_load(grid)


def find_repeating_cycle(grid):
	seen_grid_strs = {}

	for i in range(1000000000):
		tilt_north(grid)
		tilt_west(grid)
		tilt_south(grid)
		tilt_east(grid)

		grid_str = to_grid_str(grid)

		if grid_str in seen_grid_strs:
			cycle_length = i - seen_grid_strs[grid_str]
			return i + 1, cycle_length

		seen_grid_strs[grid_str] = i


def solve_part_2(grid):
	grid = grid.copy()
	seen_grid_strs = {}
	start_cycle, cycle_length = find_repeating_cycle(grid)

	cycle_count = 1000000000
	cycle_count -= start_cycle
	cycle_count %= cycle_length

	for i in range(cycle_count):
		tilt_north(grid)
		tilt_west(grid)
		tilt_south(grid)
		tilt_east(grid)

	return get_total_load(grid)


def main():
	grid = {(x, y): c for y, l in enumerate(stdin) for x, c in enumerate(l.strip())}
	print(solve_part_1(grid))
	print(solve_part_2(grid))


if __name__ == "__main__":
	main()
