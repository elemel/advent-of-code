from sys import stdin


def solve(s):
    v = 0

    for c in s:
        i = ord(c)
        v += i
        v *= 17
        v %= 256

    return v


def main():
    s = stdin.read().strip()
    ws = s.split(",")

    print(sum(solve(w) for w in ws))

    boxes = [{} for _ in range(256)]

    for w in ws:
        if "=" in w:
            a, b = w.split("=")
            i = solve(a)
            boxes[i][a] = int(b)
        elif w.endswith("-"):
            w = w.strip("-")
            i = solve(w)
            boxes[i].pop(w, None)
        else:
            assert False

    print(
        sum(
            v * (i + 1) * (j + 1)
            for i, d in enumerate(boxes)
            for j, v in enumerate(d.values())
        )
    )


if __name__ == "__main__":
    main()
