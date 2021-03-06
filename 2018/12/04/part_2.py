from collections import Counter
from sys import stdin


def main():
    lines = sorted(line.strip() for line in stdin)

    guard_id = 0
    falls_asleep_minute = 0

    asleep = Counter()

    for line in lines:
        if line.endswith(' begins shift'):
            guard_id = int(line[26:-13])
        elif line.endswith(' falls asleep'):
            falls_asleep_minute = int(line[15:17])
        elif line.endswith(' wakes up'):
            wakes_up_minute = int(line[15:17])

            for minute in range(falls_asleep_minute, wakes_up_minute):
                asleep[guard_id, minute] += 1

    [((guard_id, minute), _)] = asleep.most_common(1)
    print(guard_id * minute)


if __name__ == '__main__':
    main()
