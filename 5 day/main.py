def part1():
    arr = []
    for _ in range(1000):
        line = []
        for _ in range(1000):
            line.append(0)
        arr.append(line)

    with open("input.txt", "r") as f:
        for cords in f.readlines():
            c1, c2 = cords.strip("\n").split(" -> ")
            c1 = [int(c) for c in c1.split(",")]
            c2 = [int(c) for c in c2.split(",")]
            if c1[0] == c2[0] or c1[1] == c2[1]:
                for x in range(min(c1[0], c2[0]), max(c1[0], c2[0]) + 1):
                    for y in range(min(c1[1], c2[1]), max(c1[1], c2[1]) + 1):
                        arr[x][y] += 1

    result = 0
    for x in range(1000):
        for y in range(1000):
            if arr[x][y] >= 2:
                result += 1
    print(result)
    return arr


def part2():
    arr = part1()

    with open("input.txt", "r") as f:
        for cords in f.readlines():
            c1, c2 = cords.strip("\n").split(" -> ")
            c1 = [int(c) for c in c1.split(",")]
            c2 = [int(c) for c in c2.split(",")]
            if c1[0] != c2[0] and c1[1] != c2[1]:

                if c1[0] < c2[0] and c1[1] < c2[1]:
                    for i in range((c2[0] - c1[0]) + 1):
                        arr[c1[0] + i][c1[1] + i] += 1

                elif c1[0] > c2[0] and c1[1] < c2[1]:
                    for i in range((c1[0] - c2[0]) + 1):
                        arr[c2[0] + i][c2[1] - i] += 1

                elif c1[0] < c2[0] and c1[1] > c2[1]:
                    for i in range((c2[0] - c1[0]) + 1):
                        arr[c1[0] + i][c1[1] - i] += 1

                else:
                    for i in range((c1[0] - c2[0]) + 1):
                        arr[c2[0] + i][c2[1] + i] += 1

    result = 0
    for x in range(1000):
        for y in range(1000):
            if arr[x][y] >= 2:
                result += 1
    print(result)


def main():
    # part1()
    part2()


if __name__ == "__main__":
    main()
