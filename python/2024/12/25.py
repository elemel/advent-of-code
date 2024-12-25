from sys import stdin


def main():
    blocks = stdin.read().split("\n\n")
    print(sum(("#", "#") not in zip(l, k) for l in blocks for k in blocks) // 2)


if __name__ == "__main__":
    main()
