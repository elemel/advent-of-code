from sys import stdin
from collections import defaultdict


def parse_point(s):
    x, y, z = [int(w) for w in s.split(",")]
    return x, y, z


def parse_brick(s):
    a, b = [parse_point(p) for p in s.split("~")]
    return a, b


def generate_brick_xy_positions(brick):
    for y in range(brick[0][1], brick[1][1] + 1):
        for x in range(brick[0][0], brick[1][0] + 1):
            yield x, y


def add_3(a, b):
    ax, ay, az = a
    bx, by, bz = b

    return ax + bx, ay + by, az + bz


def move_brick(brick, offset):
    a, b = brick
    return add_3(a, offset), add_3(b, offset)


def fall_bricks(bricks):
    new_bricks = []
    ground = defaultdict(int)
    fall_count = 0

    for brick in bricks:
        xy_positions = list(generate_brick_xy_positions(brick))
        ground_max_z = max(ground[p] for p in xy_positions)
        fall_distance = brick[0][2] - ground_max_z - 1

        if fall_distance:
            brick = move_brick(brick, (0, 0, -fall_distance))
            fall_count += 1

        new_bricks.append(brick)

        for position in xy_positions:
            ground[position] = brick[1][2]

    return new_bricks, fall_count


def is_safe_brick(bricks, i):
    new_bricks = bricks[:i] + bricks[i + 1 :]
    return new_bricks == fall_bricks(new_bricks)[0]


def main():
    bricks = [parse_brick(l.strip()) for l in stdin]

    bricks.sort(key=lambda b: b[0][2])
    bricks, _ = fall_bricks(bricks)

    print(sum(is_safe_brick(bricks, i) for i in range(len(bricks))))
    print(sum(fall_bricks(bricks[:i] + bricks[i + 1 :])[1] for i in range(len(bricks))))


if __name__ == "__main__":
    main()
