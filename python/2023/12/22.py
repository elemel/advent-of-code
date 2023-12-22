from sys import stdin
from collections import defaultdict, namedtuple


def parse_point(s):
    x, y, z = [int(w) for w in s.split(",")]
    return x, y, z


def parse_brick(s):
    a, b = [parse_point(p) for p in s.split("~")]
    return a, b


def generate_horizontal_brick_positions(brick):
    a, b = brick

    ax, ay, az = a
    bx, by, bz = b

    for y in range(ay, by + 1):
        for x in range(ax, bx + 1):
            yield x, y


def add(a, b):
    ax, ay, az = a
    bx, by, bz = b

    return ax + bx, ay + by, az + bz


def move_brick(brick, offset):
    a, b = brick
    return add(a, offset), add(b, offset)


def get_brick_min_z(brick):
    return brick[0][2]


def get_brick_max_z(brick):
    return brick[1][2]


def fall_bricks(bricks):
    new_bricks = []
    ground = defaultdict(int)
    fall_count = 0

    for brick in bricks:
        horizontal_positions = list(generate_horizontal_brick_positions(brick))
        ground_max_z = max(ground[p] for p in horizontal_positions)
        fall_distance = get_brick_min_z(brick) - ground_max_z - 1

        if fall_distance:
            brick = move_brick(brick, (0, 0, -fall_distance))
            fall_count += 1

        new_bricks.append(brick)

        for position in horizontal_positions:
            ground[position] = get_brick_max_z(brick)

    return new_bricks, fall_count


def is_safe_brick(bricks, i):
    new_bricks = bricks[:i] + bricks[i + 1 :]
    return new_bricks == fall_bricks(new_bricks)[0]


def main():
    bricks = [parse_brick(l.strip()) for l in stdin]

    bricks.sort(key=get_brick_min_z)
    bricks, _ = fall_bricks(bricks)

    print(sum(is_safe_brick(bricks, i) for i in range(len(bricks))))
    print(sum(fall_bricks(bricks[:i] + bricks[i + 1 :])[1] for i in range(len(bricks))))


if __name__ == "__main__":
    main()
