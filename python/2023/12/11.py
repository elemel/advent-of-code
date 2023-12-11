from sys import stdin


def get_distance(a, b, xs, ys, expansion):
    ax, ay = a
    bx, by = b

    dx = sum(1 if x in xs else expansion for x in range(min(ax, bx), max(ax, bx)))
    dy = sum(1 if y in ys else expansion for y in range(min(ay, by), max(ay, by)))

    return dx + dy


def main():
    galaxies = {
        (x, y) for y, l in enumerate(stdin) for x, c in enumerate(l.strip()) if c != "."
    }

    xs = {x for x, y in galaxies}
    ys = {y for x, y in galaxies}

    pairs = [(a, b) for a in galaxies for b in galaxies if a < b]

    print(sum(get_distance(a, b, xs, ys, 2) for a, b in pairs))
    print(sum(get_distance(a, b, xs, ys, 1000000) for a, b in pairs))


if __name__ == "__main__":
    main()
