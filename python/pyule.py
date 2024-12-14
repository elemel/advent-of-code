from dataclasses import dataclass
from typing import Iterator, Iterable, Union
from itertools import count


@dataclass(frozen=True)
class Vector2:
    x: int
    y: int

    ZERO = None

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


def sign(i: int) -> int:
    return -1 if i < 0 else 1 if i > 0 else 0


def parse_ints(s: str) -> Iterable[int]:
    s = "".join(c if c in "-0123456789" else " " for c in s)
    return map(int, s.split())
