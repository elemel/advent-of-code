from dataclasses import dataclass
from typing import Iterator, Iterable, Union, Callable, ClassVar
from itertools import count
from heapq import heappush, heappop
from sys import maxsize
from functools import total_ordering


@dataclass(frozen=True)
@total_ordering
class Vector2:
    x: int
    y: int

    ZERO: ClassVar["Vector2"]
    ONE: ClassVar["Vector2"]

    UP_LEFT: ClassVar["Vector2"]
    UP: ClassVar["Vector2"]
    UP_RIGHT: ClassVar["Vector2"]
    LEFT: ClassVar["Vector2"]
    RIGHT: ClassVar["Vector2"]
    DOWN_LEFT: ClassVar["Vector2"]
    DOWN: ClassVar["Vector2"]
    DOWN_RIGHT: ClassVar["Vector2"]

    NORTHWEST: ClassVar["Vector2"]
    NORTH: ClassVar["Vector2"]
    NORTHEAST: ClassVar["Vector2"]
    WEST: ClassVar["Vector2"]
    EAST: ClassVar["Vector2"]
    SOUTHWEST: ClassVar["Vector2"]
    SOUTH: ClassVar["Vector2"]
    SOUTHEAST: ClassVar["Vector2"]

    DIRECTIONS: ClassVar[set["Vector2"]]
    ORTHOGONAL_DIRECTIONS: ClassVar[set["Vector2"]]
    DIAGONAL_DIRECTIONS: ClassVar[set["Vector2"]]

    def __neg__(self) -> "Vector2":
        return Vector2(-self.x, -self.y)

    def __pos__(self) -> "Vector2":
        return self

    def __add__(self, other: "Vector2") -> "Vector2":
        if not isinstance(other, Vector2):
            return NotImplemented

        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector2") -> "Vector2":
        if not isinstance(other, Vector2):
            return NotImplemented

        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[int, "Vector2"]) -> "Vector2":
        if isinstance(other, int):
            # Scalar multiplication
            return Vector2(self.x * other, self.y * other)
        elif isinstance(other, Vector2):
            # Element-wise multiplication
            return Vector2(self.x * other.x, self.y * other.y)
        else:
            return NotImplemented

    def __rmul__(self, other: int) -> "Vector2":
        return self.__mul__(other)

    def __floordiv__(self, other: Union[int, "Vector2"]) -> "Vector2":
        if isinstance(other, int):
            # Scalar floor division
            return Vector2(self.x // other, self.y // other)
        elif isinstance(other, Vector2):
            # Element-wise floor division
            return Vector2(self.x // other.x, self.y // other.y)
        else:
            return NotImplemented

    def __mod__(self, other: Union[int, "Vector2"]) -> "Vector2":
        if isinstance(other, int):
            # Scalar modulus
            return Vector2(self.x % other, self.y % other)
        elif isinstance(other, Vector2):
            # Element-wise modulus
            return Vector2(self.x % other.x, self.y % other.y)
        else:
            return NotImplemented

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector2):
            return False

        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __repr__(self) -> str:
        return f"Vector2(x={self.x}, y={self.y})"

    def __len__(self) -> int:
        return 2

    def __getitem__(self, index: int) -> int:
        return (self.x, self.y)[index]

    def __iter__(self) -> Iterator[int]:
        return iter((self.x, self.y))

    def __bool__(self) -> bool:
        return bool(self.x or self.y)

    def __lt__(self, other: "Vector2") -> bool:
        return (self.x, self.y) < (other.x, other.y)

    def dot(self, other: "Vector2") -> int:
        if not isinstance(other, Vector2):
            return NotImplemented

        return self.x * other.x + self.y * other.y

    def cross(self, other: "Vector2") -> int:
        if not isinstance(other, Vector2):
            return NotImplemented

        return self.x * other.y - self.y * other.x

    def turn_left(self) -> "Vector2":
        return Vector2(self.y, -self.x)

    def turn_right(self) -> "Vector2":
        return Vector2(-self.y, self.x)

    def sign(self) -> "Vector2":
        return Vector2(sign(self.x), sign(self.y))


Vector2.ZERO = Vector2(0, 0)
Vector2.ONE = Vector2(1, 1)

Vector2.UP_LEFT = Vector2(-1, -1)
Vector2.UP = Vector2(0, -1)
Vector2.UP_RIGHT = Vector2(1, -1)
Vector2.LEFT = Vector2(-1, 0)
Vector2.RIGHT = Vector2(1, 0)
Vector2.DOWN_LEFT = Vector2(-1, 1)
Vector2.DOWN = Vector2(0, 1)
Vector2.DOWN_RIGHT = Vector2(1, 1)

Vector2.NORTHWEST = Vector2(-1, -1)
Vector2.NORTH = Vector2(0, -1)
Vector2.NORTHEAST = Vector2(1, -1)
Vector2.WEST = Vector2(-1, 0)
Vector2.EAST = Vector2(1, 0)
Vector2.SOUTHWEST = Vector2(-1, 1)
Vector2.SOUTH = Vector2(0, 1)
Vector2.SOUTHEAST = Vector2(1, 1)

Vector2.DIRECTIONS = {
    Vector2.NORTHWEST,
    Vector2.NORTH,
    Vector2.NORTHEAST,
    Vector2.WEST,
    Vector2.EAST,
    Vector2.SOUTHWEST,
    Vector2.SOUTH,
    Vector2.SOUTHEAST,
}

Vector2.ORTHOGONAL_DIRECTIONS = {
    Vector2.NORTH,
    Vector2.WEST,
    Vector2.EAST,
    Vector2.SOUTH,
}

Vector2.DIAGONAL_DIRECTIONS = {
    Vector2.NORTHWEST,
    Vector2.NORTHEAST,
    Vector2.SOUTHWEST,
    Vector2.SOUTHEAST,
}


def parse_grid(lines: Iterable[str]) -> dict[Vector2, str]:
    return {
        Vector2(x, y): char
        for y, line in enumerate(lines)
        for x, char in enumerate(line.strip())
    }


def sign(i: int) -> int:
    return -1 if i < 0 else 1 if i > 0 else 0


def parse_ints(s: str) -> Iterable[int]:
    s = "".join(c if c in "-0123456789" else " " for c in s)
    return map(int, s.split())


def print_grid(grid: dict[Vector2, str], default: str = ".") -> None:
    if not grid:
        return

    min_x = min(position.x for position in grid)
    max_x = max(position.x for position in grid)
    min_y = min(position.y for position in grid)
    max_y = max(position.y for position in grid)

    for y in range(min_y, max_y + 1):
        print(
            "".join(grid.get(Vector2(x, y), default) for x in range(min_x, max_x + 1))
        )


def dijkstra[
    T
](
    graph: Union[dict[T, dict[T, int]], Callable[[T], dict[T, int]]],
    starts: Iterable[T],
    goals: Union[set[T], Callable[[T], bool]] = [],
) -> tuple[dict[T, int], dict[T, set[T]]]:
    if not callable(graph):
        graph = graph.__getitem__

    if not callable(goals):
        goals = goals.__contains__

    goal_distance = maxsize
    distances = {}
    parents = {}
    queue: list[tuple[int, T]] = []

    for node in starts:
        distances[node] = 0
        parents[node] = set[T]()
        heappush(queue, (0, node))

    while queue:
        distance, node = heappop(queue)

        if distance > goal_distance:
            break

        if distance > distances.get(node, maxsize):
            continue

        if goals(node):
            goal_distance = min(goal_distance, distance)
            continue

        for new_node, weight in graph(node).items():
            new_distance = distance + weight
            min_distance = distances.get(new_node, maxsize)

            if new_distance < min_distance:
                distances[new_node] = new_distance
                parents[new_node] = {node}
                heappush(queue, (new_distance, new_node))
            elif new_distance == min_distance:
                parents[new_node].add(node)

    return distances, parents


def get_ancestors[T](parents: dict[T, set[T]], nodes: set[T]) -> set[T]:
    result = set()

    def impl(node):
        if node in result:
            return

        result.add(node)

        for parent in parents[node]:
            impl(parent)

    for node in nodes:
        impl(node)

    return result
