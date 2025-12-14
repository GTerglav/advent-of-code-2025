def sol1(lines):
    zero_count = 0
    position = 50
    for line in lines:
        direction = line[0] == "R"
        amount = int(line[1:])

        if direction:
            position = (position + amount) % 100
        else:
            position = (position - amount) % 100

        if position == 0:
            zero_count += 1

    return zero_count


def sol2(lines):
    zero_count = 0
    position = 50

    for line in lines:
        direction = line[0] == "R"
        amount = int(line[1:])

        full_rot = amount // 100
        partial_rot = amount % 100
        zero_count += full_rot

        if partial_rot > 0:
            if direction:
                if partial_rot + position >= 100:
                    zero_count += 1
                position = (position + partial_rot) % 100
            else:
                if position - partial_rot <= 0 and position != 0:
                    zero_count += 1
                position = (position - partial_rot) % 100

    return zero_count


if __name__ == "__main__":
    with open("input1.txt", encoding="utf-8") as file:
        data = file.read().splitlines()

    print(f"Part one: {sol1(data)}")
    print(f"Part two: {sol2(data)}")
