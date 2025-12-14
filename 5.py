def join(current, ranges):
    join_happened = False
    idx = 0

    for i, r in enumerate(ranges):
        if (
            current[0] <= r[0] <= current[1]
            or current[0] <= r[1] <= current[1]
            or (r[0] <= current[0] and current[1] <= r[1])
            or (current[0] <= r[0] and current[1] >= r[1])
        ):
            current = (min(current[0], r[0]), max(current[1], r[1]))
            join_happened = True
            idx = i
            break

    if join_happened:
        ranges.pop(idx)

    return current, ranges, join_happened


def sol(lines, part):
    ranges = []
    produce = []
    for line in lines:
        if line != "":
            res = line.split("-")
            if len(res) == 1:
                produce.append(int(res[0]))
            else:
                ranges.append((int(res[0]), int(res[1])))

    if part == 1:
        fresh = {}
        for product in produce:
            for r in ranges:
                if int(r[0]) <= int(product) <= int(r[1]):
                    fresh[product] = 1
                    break

        return len(fresh)

    full_ranges = []
    current = ranges[0]
    ranges.pop(0)

    while True:
        current, ranges, join_happened = join(current, ranges)

        if not join_happened:
            full_ranges.append(current)
            if len(ranges) == 0:
                break

            current = ranges[0]
            ranges.pop(0)

    return sum(end + 1 - start for start, end in full_ranges)


if __name__ == "__main__":
    with open("input5.txt", encoding="utf-8") as file:
        data = file.read().splitlines()

    print(f"Part one: {sol(data, 1)}")
    print(f"Part two: {sol(data, 2)}")
