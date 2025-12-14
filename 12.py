def sol1(lines):
    shape_sizes = []
    inc = 0

    for line in lines:
        if "#" in line:
            inc += 1
            count = line.count("#")
            if inc == 1:
                shape_sizes.append(count)
            else:
                shape_sizes[-1] += count

            inc %= 3

    total = 0

    for line in lines:
        if "x" in line:
            parts = line.split()

            width, height = map(int, parts[0][:-1].split("x"))
            dimension = width * height

            space_taken = sum(
                int(parts[i + 1]) * shape_sizes[i] for i in range(len(parts) - 1)
            )

            if space_taken <= dimension:
                total += 1

    return total


if __name__ == "__main__":
    with open("input12.txt", encoding="utf-8") as file:
        data = file.read().splitlines()

    print(f"Part one: {sol1(data)}")
