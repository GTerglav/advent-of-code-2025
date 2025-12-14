def euclidean_distance(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2


def sol(lines, part):
    boxes = [list(map(int, line.split(","))) for line in lines]

    distances = [
        (euclidean_distance(box1, box2), i, j)
        for i, box1 in enumerate(boxes)
        for j, box2 in enumerate(boxes)
        if i < j
    ]
    distances.sort()

    circuits = {}
    lengths = []
    label = 1
    output = 0
    i = 0
    while len(lengths) == 0 or lengths[-1] != 1000:
        s1, s2 = distances[i][1], distances[i][2]

        if s1 not in circuits and s2 not in circuits:
            circuits[s1] = label
            circuits[s2] = label
            label += 1

        elif s1 not in circuits:
            circuits[s1] = circuits[s2]

        elif s2 not in circuits:
            circuits[s2] = circuits[s1]

        elif circuits[s2] != circuits[s1]:
            value_to_change = circuits[s2]

            for key, val in circuits.items():
                if val == value_to_change:
                    circuits[key] = circuits[s1]

        circuit_lengths = {}
        for oz in circuits.values():
            if oz in circuit_lengths:
                circuit_lengths[oz] += 1
            else:
                circuit_lengths[oz] = 1

        lengths = []
        for length in circuit_lengths.values():
            lengths.append(length)
        lengths.sort()

        if part == 1 and i == 1000:
            return lengths[-1] * lengths[-2] * lengths[-3]

        output = int(boxes[s1][0]) * int(boxes[s2][0])
        i += 1

    return output


if __name__ == "__main__":
    with open("input8.txt", encoding="utf-8") as file:
        data = file.read().splitlines()

    print(f"Part one: {sol(data, 1)}")
    print(f"Part two: {sol(data, 2)}")
