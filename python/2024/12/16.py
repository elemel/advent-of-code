from sys import stdin, maxsize
from pyule import parse_grid, Vector2, dijkstra, get_ancestors
from functools import cache


def main():
    grid = parse_grid(stdin)

    [start] = [position for position, char in grid.items() if char == "S"]
    [end] = [position for position, char in grid.items() if char == "E"]

    @cache
    def graph(state):
        position, direction = state
        result = {}

        if grid[position + direction] != "#":
            result[position + direction, direction] = 1

        for new_direction in [direction.turn_left(), direction.turn_right()]:
            result[position, new_direction] = 1000

        return result

    goals = {(end, direction) for direction in Vector2.ORTHOGONAL_DIRECTIONS}
    distances, parents = dijkstra(graph, [(start, Vector2.EAST)])
    min_distance = min(distances[goal] for goal in goals)
    print(min_distance)

    best_goals = [goal for goal in goals if distances[goal] == min_distance]
    print(len({position for position, direction in get_ancestors(parents, best_goals)}))


if __name__ == "__main__":
    main()
