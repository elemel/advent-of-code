from sys import stdin
from pyule import parse_grid, Vector2, dijkstra


def main():
    grid = parse_grid(stdin)

    [start] = [position for position in grid if grid[position] == "S"]
    [end] = [position for position in grid if grid[position] == "E"]

    def graph(position):
        result = {}

        for direction in Vector2.ORTHOGONAL_DIRECTIONS:
            neighbor = position + direction

            if grid.get(neighbor, "#") != "#": 
                result[neighbor] = 1

        return result

    distances, parents = dijkstra(graph, {start})

    answer_1 = 0
    answer_2 = 0

    for a in distances:
        for b in distances:
            cheat_distance = (b - a).manhattan_length()

            if distances[b] - distances[a] - cheat_distance >= 100:
                if cheat_distance <= 2:
                    answer_1 += 1

                if cheat_distance <= 20:
                    answer_2 += 1

    print(answer_1)
    print(answer_2)


if __name__ == "__main__":
    main()
