from sys import stdin
from math import lcm

def parse_node(line):
    name, children_str = line.split("=")
    name = name.strip()
    children_str = children_str.split("(")[1].split(")")[0]
    left_name, right_name = [w.strip() for w in children_str.split(",")]
    return name, (left_name, right_name)


def get_distance(path, nodes, position, destination):
    distance = 0

    while position != destination:
        step = path[distance % len(path)]
        position = nodes[position][step == "R"]
        distance += 1

    return distance


def get_ghost_distances(path, nodes, position):
    visited = set()
    distance = 0
    ghost_distances = {}

    while (distance % len(path), position) not in visited:
        visited.add((distance % len(path), position))

        step = path[distance % len(path)]
        position = nodes[position][step == "R"]
        distance += 1

        if position.endswith("Z"):
            ghost_distances[position] = distance

    return ghost_distances


def main():
    path_str, nodes_str = stdin.read().split("\n\n")
    path = path_str.strip()
    nodes = [parse_node(l) for l in nodes_str.splitlines()]
    nodes = {n: c for n, c in nodes}

    print(get_distance(path, nodes, "AAA", "ZZZ"))

    ghost_positions = sorted(p for p in nodes.keys() if p.endswith("A"))
    ghost_distances = [min(get_ghost_distances(path, nodes, p).values()) for p in ghost_positions]
    print(lcm(*ghost_distances))


if __name__ == "__main__":
    main()
