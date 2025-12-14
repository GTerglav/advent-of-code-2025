def sol1(lines):
    start = (0, lines[0].index("S"))
    hit_splits = {}
    beams = [start]

    while len(beams) > 0:
        to_remove = []
        to_add = []

        for beam in beams:
            i, j = beam[0], beam[1]
            while 0 <= i + 1 < len(lines):
                i += 1
                if lines[i][j] != "^":
                    continue

                if (i, j) not in hit_splits:
                    hit_splits[(i, j)] = True
                    if 0 <= j - 1 < len(lines[0]):
                        to_add.append((i, j - 1))
                    if 0 <= j + 1 < len(lines[0]):
                        to_add.append((i, j + 1))
                break

            to_remove.append(beam)

        beams = [x for x in beams if x not in to_remove]
        for beam in to_add:
            if beam not in beams:
                beams.append(beam)

    return len(hit_splits)


def add_beam(beam, beams):
    added = False
    for b in beams:
        if b[0] == beam[0] and b[1] == beam[1]:
            b[2] += beam[2]
            added = True
            break

    if not added:
        beams.append(beam)

    return beams


def sol2(lines):
    start = (0, lines[0].index("S"), 1)
    beams = [start]
    distinct_beams = 1

    while len(beams) > 0:
        to_remove = []
        to_add = []

        # compute all the beams in one row before moving to the next row.
        beams.sort()
        for idx, beam in enumerate([x for x in beams if x[0] == min(beams)[0]]):
            i, j, k = beam[0], beam[1], beam[2]

            while 0 <= i + 1 < len(lines):
                i += 1

                if lines[i][j] != "^":
                    continue

                distinct_beams -= k
                if 0 <= j - 1 < len(lines[0]):
                    to_add.append([i, j - 1, k])
                    distinct_beams += k
                if 0 <= j + 1 < len(lines[0]):
                    to_add.append([i, j + 1, k])
                    distinct_beams += k
                break

            to_remove.append(idx)

        to_remove.sort(reverse=True)
        for i in to_remove:
            beams.pop(i)

        for beam in to_add:
            beams = add_beam(beam, beams)

    return distinct_beams


if __name__ == "__main__":
    with open("input7.txt", encoding="utf-8") as file:
        data = file.read().splitlines()

    print(f"Part one: {sol1(data)}")
    print(f"Part two: {sol2(data)}")
