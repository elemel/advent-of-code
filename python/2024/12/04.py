from sys import stdin

DIRECTIONS = [(dx, dy) for dy in [-1, 0, 1] for dx in [-1, 0, 1] if dx or dy]


def match_word(grid, position, direction, word):
    x, y = position
    dx, dy = direction
    return all(grid.get((x + i * dx, y + i * dy)) == c for i, c in enumerate(word))


def match_word_cross(grid, position, word):
    x, y = position
    left, middle, right = word

    northwest = grid.get((x - 1, y - 1))
    northeast = grid.get((x + 1, y - 1))

    center = grid.get(position)

    southwest = grid.get((x - 1, y + 1))
    southeast = grid.get((x + 1, y + 1))

    return (
        center == middle
        and {northwest, southeast} == {left, right}
        and {southwest, northeast} == {left, right}
    )


def main():
    grid = {
        (x, y): c for y, line in enumerate(stdin) for x, c in enumerate(line.strip())
    }
    print(
        sum(
            match_word(grid, position, direction, "XMAS")
            for position in grid
            for direction in DIRECTIONS
        )
    )
    print(sum(match_word_cross(grid, position, "MAS") for position in grid))


if __name__ == "__main__":
    main()
