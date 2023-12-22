from sys import stdin


def parse_point(s):
    x, y, z = [int(w) for w in s.split(",")]
    return x, y, z


def parse_brick(s):
    a, b = [parse_point(p) for p in s.split("~")]
    return a, b


def get_brick_min_z(brick):
    return brick[0][2]


def fall_bricks(bricks):
    new_bricks = []
    grid = set()

    for brick in bricks:
        while True:
            if brick[0][2] == 1:
                break

            if any(
                (x, y, brick[0][2] - 1) in grid
                for y in range(brick[0][1], brick[1][1] + 1)
                for x in range(brick[0][0], brick[1][0] + 1)
            ):
                break

            brick = (brick[0][0], brick[0][1], brick[0][2] - 1), (
                brick[1][0],
                brick[1][1],
                brick[1][2] - 1,
            )

        new_bricks.append(brick)

        for z in range(brick[0][2], brick[1][2] + 1):
            for y in range(brick[0][1], brick[1][1] + 1):
                for x in range(brick[0][0], brick[1][0] + 1):
                    grid.add((x, y, z))

    return new_bricks


def fall_bricks_2(bricks):
    new_bricks = []
    grid = set()
    fall_count = 0

    for brick in bricks:
        fall_distance = 0

        while True:
            if brick[0][2] == 1:
                break

            if any(
                (x, y, brick[0][2] - 1) in grid
                for y in range(brick[0][1], brick[1][1] + 1)
                for x in range(brick[0][0], brick[1][0] + 1)
            ):
                break

            brick = (brick[0][0], brick[0][1], brick[0][2] - 1), (
                brick[1][0],
                brick[1][1],
                brick[1][2] - 1,
            )

            fall_distance += 1

        new_bricks.append(brick)

        for z in range(brick[0][2], brick[1][2] + 1):
            for y in range(brick[0][1], brick[1][1] + 1):
                for x in range(brick[0][0], brick[1][0] + 1):
                    grid.add((x, y, z))

        if fall_distance:
            fall_count += 1

    return new_bricks, fall_count


def is_safe_brick(bricks, i):
    new_bricks = bricks[:i] + bricks[i + 1:]
    return new_bricks == fall_bricks(new_bricks)


def main():
    bricks = [parse_brick(l.strip()) for l in stdin]

    bricks.sort(key=get_brick_min_z)
    bricks = fall_bricks(bricks)

    print(sum(is_safe_brick(bricks, i) for i in range(len(bricks))))
    print(sum(fall_bricks_2(bricks[:i] + bricks[i + 1:])[1] for i in range(len(bricks))))


if __name__ == "__main__":
    main()
