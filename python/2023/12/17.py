from sys import stdin
from heapq import heappop, heappush


DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def add(a, b):
    ax, ay = a
    bx, by = b

    return ax + bx, ay + by


def neg(a):
    ax, ay = a
    return -ax, -ay


def solve(grid, min_streak, max_streak):
    min_x = min(x for x, y in grid)
    min_y = min(y for x, y in grid)

    max_x = max(x for x, y in grid)
    max_y = max(y for x, y in grid)

    queue = []
    heappush(queue, (0, ((0, 0), (0, 0), 0)))
    min_costs = {}

    while queue:
        cost, state = heappop(queue)

        if state in min_costs and min_costs[state] <= cost:
            continue

        min_costs[state] = cost
        position, direction, streak = state

        if position == (max_x, max_y) and streak >= min_streak:
            return cost

        for new_direction in DIRECTIONS:
            if new_direction == neg(direction):
                continue

            new_position = add(position, new_direction)

            if new_position not in grid:
                continue

            new_cost = cost + grid[new_position]
            new_streak = streak + 1 if new_direction == direction else 1

            if streak and new_direction != direction and streak < min_streak:
                continue

            if new_direction == direction and new_streak > max_streak:
                continue

            new_state = new_position, new_direction, new_streak

            if new_state in min_costs and min_costs[new_state] <= new_cost:
                continue

            heappush(queue, (new_cost, new_state))

    return None


def main():
    grid = {
        (x, y): int(c) for y, l in enumerate(stdin) for x, c in enumerate(l.strip())
    }
    print(solve(grid, 1, 3))
    print(solve(grid, 4, 10))


if __name__ == "__main__":
    main()
