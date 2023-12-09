from sys import stdin


def extrapolate(history):
    if not history:
        return 0

    diffs = [b - a for a, b in zip(history[:-1], history[1:])]
    return history[-1] + extrapolate(diffs)


def main():
    histories = [[int(w) for w in l.split()] for l in stdin]

    print(sum(extrapolate(h) for h in histories))
    print(sum(extrapolate(h[::-1]) for h in histories))


if __name__ == "__main__":
    main()
