from math import fabs


def part1():
    with open("input.txt", "r") as f:
        for line in f.readlines():
            arr = [int(x) for x in line.strip("\n").split(",")]

    sums = []
    for i in range(len(arr)):
        s = []
        for x in range(len(arr)):
            s.append(fabs(arr[x] - i))
        sums.append(sum(s))

    print(min(sums))
    return arr


def part2():
    arr = part1()

    sums = []
    for i in range(len(arr)):
        s = []
        for x in range(len(arr)):
            distance = int(fabs(arr[x] - i))
            s.append(sum([x for x in range(1, distance + 1)]))
        sums.append(sum(s))

    print(min(sums))


def main():
    # part1()
    part2()


if __name__ == "__main__":
    main()
