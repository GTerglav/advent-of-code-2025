def sol1(lines):
    total = 0
    for line in lines:
        line = line[:-1]
        maks = 0

        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                number = 10 * int(line[i]) + int(line[j])
                if number > maks:
                    maks = number

        total += maks

    return total


def choose_first_dig(line, num_remaining):
    n = len(line)
    diff = n - num_remaining + 1
    max_digit = max(line[:diff])
    position = line[:diff].index(max_digit)
    return max_digit, position


def sol2(lines):
    total = 0
    for line in lines:
        line = line[:-1]
        digits = []

        for i in range(12):
            maks, index = choose_first_dig(line, 12 - i)
            digits.append(maks)
            line = line[index + 1 :]

        total += int("".join(str(x) for x in digits))

    return total


if __name__ == "__main__":
    with open("input3.txt", encoding="utf-8") as file:
        data = file.read().splitlines()

    print(f"Part one: {sol1(data)}")
    print(f"Part two: {sol2(data)}")
