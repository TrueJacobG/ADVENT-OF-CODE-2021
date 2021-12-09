def check_position(arr, x, y):
    if x == 0 or x == len(arr) - 1 or y == 0 or y == len(arr[x]) - 1:
        # corners
        if x == 0 and y == 0:
            return arr[x][y] < arr[x][y + 1] and arr[x][y] < arr[x + 1][y]
        if x == 0 and y == len(arr[x]) - 1:
            return arr[x][y] < arr[x][y - 1] and arr[x][y] < arr[x + 1][y]
        if x == len(arr) - 1 and y == 0:
            return arr[x][y] < arr[x][y + 1] and arr[x][y] < arr[x - 1][y]
        if x == len(arr) - 1 and y == len(arr[x]) - 1:
            return arr[x][y] < arr[x][y - 1] and arr[x][y] < arr[x - 1][y]

        if x == 0:
            return (
                arr[x][y] < arr[x][y - 1]
                and arr[x][y] < arr[x][y + 1]
                and arr[x][y] < arr[x + 1][y]
            )

        if x == len(arr) - 1:
            return (
                arr[x][y] < arr[x][y - 1]
                and arr[x][y] < arr[x][y + 1]
                and arr[x][y] < arr[x - 1][y]
            )

        if y == 0:
            return (
                arr[x][y] < arr[x - 1][y]
                and arr[x][y] < arr[x + 1][y]
                and arr[x][y] < arr[x][y + 1]
            )

        if y == len(arr[x]) - 1:
            return (
                arr[x][y] < arr[x - 1][y]
                and arr[x][y] < arr[x + 1][y]
                and arr[x][y] < arr[x][y - 1]
            )

    else:
        return (
            arr[x][y] < arr[x - 1][y]
            and arr[x][y] < arr[x + 1][y]
            and arr[x][y] < arr[x][y - 1]
            and arr[x][y] < arr[x][y + 1]
        )


def part1():
    arr = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            arr.append([int(x) for x in list(line.strip("\n"))])

    s = 0
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if check_position(arr, x, y):
                s += 1 + arr[x][y]

    print(s)
    return arr


def flood_fill(x, y):
    global arr
    global seen

    if x < 0 or y < 0:
        return 0

    if x >= len(arr) or y >= len(arr[x]):
        return 0
        

    if arr[x][y] == 1 and not seen[x][y]:
        seen[x][y] = True
        try:
            return (
                1
                + flood_fill(x, y - 1)
                + flood_fill(x, y + 1)
                + flood_fill(x - 1, y)
                + flood_fill(x + 1, y)
            )
        except:
            return 0
    return 0


def part2():
    global arr
    global seen

    arr = part1()
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if arr[x][y] != 9:
                arr[x][y] = 1

    seen = []
    for x in range(len(arr)):
        line = []
        for y in range(len(arr[x])):
            line.append(False)
        seen.append(line)

    results = []
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            results.append(flood_fill(x, y))

    result = sorted(results, reverse=True)
    print(result[0] * result[1] * result[2])


def main():
    # part1()
    part2()


if __name__ == "__main__":
    main()
