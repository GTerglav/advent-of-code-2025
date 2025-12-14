def sol1(lines):
    line = lines[0]
    line = line.split(",")

    total = 0
    for interval in line:
        ran = interval.split("-")
        st, fin = int(ran[0]), int(ran[1])

        for number in range(st, fin + 1):
            str_number = str(number)
            n = len(str_number)
            
            if n % 2 == 0 and str_number[(n // 2) :] == str_number[: (n // 2)]:
                total += number

    return total


def sol2(lines):
    line = lines[0]
    line = line.split(",")

    total = 0
    for interval in line:
        ran = interval.split("-")
        st, fin = int(ran[0]), int(ran[1])

        for number in range(st, fin + 1):
            str_number = str(number)
            n = len(str_number)

            for i in range(1, n):
                if n % i == 0 and str_number == n // i * str_number[:i]:
                    total += number
                    break

    return total


if __name__ == "__main__":
    with open("input2.txt", encoding="utf-8") as file:
        data = file.read().splitlines()

    print(f"Part one: {sol1(data)}")
    print(f"Part two: {sol2(data)}")
