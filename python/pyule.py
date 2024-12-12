from dataclasses import dataclass
from typing import Iterator, Iterable
from itertools import count


@dataclass(frozen=True)
class Vector2:
    x: int
    y: int

    UP = None
    LEFT = None
    RIGHT = None
    DOWN = None

    NORTHWEST = None
    NORTH = None
    NORTHEAST = None
    WEST = None
    EAST = None
    SOUTHWEST = None
    SOUTH = None
    SOUTHEAST = None

    DIRECTIONS = None
    ORTHOGONAL_DIRECTIONS = None
    DIAGONAL_DIRECTIONS = None

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

    def __mul__(self, scalar: int) -> "Vector2":
        if not isinstance(scalar, int):
            return NotImplemented

        return Vector2(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: int) -> "Vector2":
        return self.__mul__(scalar)

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

    def __iter__(self) -> Iterator[int]:
        return iter((self.x, self.y))

    def turn_left(self) -> "Vector2":
        return Vector2(self.y, -self.x)

    def turn_right(self) -> "Vector2":
        return Vector2(-self.y, self.x)


Vector2.UP = Vector2(0, -1)
Vector2.LEFT = Vector2(-1, 0)
Vector2.RIGHT = Vector2(1, 0)
Vector2.DOWN = Vector2(0, 1)

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
