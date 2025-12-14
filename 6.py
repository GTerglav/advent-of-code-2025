def sol1(lines):
    rows = len(lines)
    total = 0

    operations = {}
    counter = 0
    for char in lines[rows - 1]:
        if char != " ":
            operations[counter] = char
            counter += 1

    newlines = []
    for line in lines:
        newlines.append(line.split(" "))

    def find_number(numbers, n):
        counter = 0
        for e in numbers:
            if e != "":
                if counter == n:
                    return int(e)
                counter += 1

        raise ValueError("number not found")

    for key, value in operations.items():
        result = 0
        for i in range(rows - 1):
            number = find_number(newlines[i], key)
            if value == "*":
                result = max(number, result * number)
            else:
                result += number
        total += result

    return total


def sol2(lines):
    rows = len(lines)
    cols = len(lines[0])

    total = 0

    operations = {}
    counter = 0
    for i, char in enumerate(lines[rows - 1]):
        if char != " ":
            following_spaces = 0
            j = 1
            while i + j < cols and lines[rows - 1][i + j] == " ":
                following_spaces += 1
                j += 1
            operations[counter] = (char, following_spaces, i)

            counter += 1

    def find_number(lines, column):
        r = len(lines)
        hit_number = False
        number = ""

        for i in range(r - 1):
            if lines[i][column] != " ":
                hit_number = True
                number += lines[i][column]
            if lines[i][column] == " " and hit_number:
                break

        return int(number)

    for key, value in operations.items():
        result = 0
        operation = value[0]
        following_spaces = value[1]

        if key == len(operations) - 1:
            following_spaces += 1

        location = value[2]
        for i in range(following_spaces):
            number = find_number(lines, i + location)
            if operation == "*":
                result = max(number, result * number)
            else:
                result += number

        total += result

    return total


if __name__ == "__main__":
    with open("input6.txt", encoding="utf-8") as file:
        data = file.read().splitlines()

    print(f"Part one: {sol1(data)}")
    print(f"Part two: {sol2(data)}")
