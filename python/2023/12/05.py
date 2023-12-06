from sys import stdin


def get_map_source(m):
    md, ms, mn = m
    return ms


def parse_map(s):
    return [[int(w) for w in line.split()] for line in s.strip().splitlines()[1:]]


def sort_map(m):
    return sorted(m, key=get_map_source)


def convert(map_, source):
    for map_dest, map_source, map_len in map_:
        if map_source <= source < map_source + map_len:
            return map_dest + source - map_source

    return source


def convert_range(map_range, source_range):
    map_dest, map_source, map_len = map_range
    source_start, source_len = source_range

    before_len = min(max(map_source - source_start, 0), source_len)

    mapped_len = min(
        max(map_source + map_len - source_start - before_len, 0),
        source_len - before_len,
    )

    after_len = min(
        max(
            source_start + before_len + mapped_len + source_len - map_source - map_len,
            0,
        ),
        source_len - before_len - mapped_len,
    )

    return (
        (source_start, before_len),
        (source_start + before_len - map_source + map_dest, mapped_len),
        [source_start + before_len + mapped_len, after_len],
    )


def convert_ranges(map_, source_ranges):
    dest_ranges = []

    for source_start, source_len in source_ranges:
        for map_range in map_:
            (
                (before_start, before_len),
                (mapped_start, mapped_len),
                (source_start, source_len),
            ) = convert_range(map_range, (source_start, source_len))

            if before_len:
                dest_ranges.append((before_start, before_len))

            if mapped_len:
                dest_ranges.append((mapped_start, mapped_len))

        if source_len:
            dest_ranges.append((source_start, source_len))

    return dest_ranges


def solve_part_1(maps, seeds):
    dests = seeds

    for map_ in maps:
        dests = [convert(map_, r) for r in dests]

    return min(dests)


def solve_part_2(maps, seeds):
    dest_ranges = [*zip(seeds[::2], seeds[1::2])]

    for map_ in maps:
        dest_ranges = convert_ranges(map_, dest_ranges)

    return min(s for s, l in dest_ranges)


def main():
    seeds_str, *map_strs = stdin.read().split("\n\n")
    seeds = [int(s) for s in seeds_str.split()[1:]]
    maps = [sort_map(parse_map(s)) for s in map_strs]

    print(solve_part_1(maps, seeds))
    print(solve_part_2(maps, seeds))


if __name__ == "__main__":
    main()
