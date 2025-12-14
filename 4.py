def count_neighbors(lines, i, j, removed_rolls):
    adj = [-1, 0, 1]
    count = 0

    for k in adj:
        for l in adj:
            if (k, l) == (0, 0):
                continue

            ni, nj = i + k, j + l
            if 0 <= ni < len(lines) and 0 <= nj < len(lines[0]):
                if lines[ni][nj] == "@" and (ni, nj) not in removed_rolls:
                    count += 1

    return count


def sol(lines, part):
    total = 0
    removed = {}
    any_removed = True

    while any_removed:
        any_removed = False

        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if char != "@" or (i, j) in removed:
                    continue

                neighbors = count_neighbors(lines, i, j, removed)

                if neighbors < 4:
                    if part == 2:
                        removed[(i, j)] = True
                    any_removed = True
                    total += 1

        if part == 1:
            break

    return total


if __name__ == "__main__":
    with open("input4.txt", encoding="utf-8") as file:
        data = file.read().splitlines()

    print(f"Part one: {sol(data, 1)}")
    print(f"Part two: {sol(data, 2)}")
