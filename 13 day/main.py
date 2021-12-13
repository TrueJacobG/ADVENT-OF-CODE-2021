def parse():
    arr = []
    for x in range(895):
        line = []
        for y in range(1311):
            line.append(".")
        arr.append(line)

    with open("input1.txt", "r") as f:
        for line in f.readlines():
            m, n = [int(x) for x in line.strip("\n").split(",")]
            arr[n][m] = "#"

    return arr


def count(arr):
    counter = 0
    for x in range(len(arr)):
        for y in range(len(arr[0])):
            if arr[x][y] == "#":
                counter += 1
    print(counter)


def parse_folds():
    folds = []
    with open("input2.txt", "r") as f:
        for line in f.readlines():
            line = line.strip("\n")
            l = []
            l.append(line[0])
            l.append(int(line[2:]))
            folds.append(l)
    return folds


def make_fold(arr, fold, prev_fold):
    if fold[0] == "x":
        for x in range(len(arr)):
            for y in range(prev_fold - 1, fold[1], -1):
                if arr[x][y] == "#":
                    arr[x][prev_fold - 1 - y] = "#"

        for x in range(len(arr)):
            for y in range(fold[1] + 1, prev_fold):
                arr[x][y] = "."

    if fold[0] == "y":
        for x in range(prev_fold - 1, fold[1], -1):
            for y in range(len(arr[0])):
                if arr[x][y] == "#":
                    arr[prev_fold - 1 - x][y] = "#"

        for x in range(fold[1] + 1, prev_fold):
            for y in range(len(arr[0])):
                arr[x][y] = "."

    return arr


def part1():
    arr = parse()

    folds = parse_folds()

    arr = make_fold(arr, folds[0])
    count(arr)


def part2():
    arr = parse()
    folds = parse_folds()

    prev_foldx = len(arr[0])
    prev_foldy = len(arr)

    for fold in folds:

        if fold[0] == "x":
            arr = make_fold(arr, fold, prev_foldx)
            prev_foldx = fold[1]
        else:
            arr = make_fold(arr, fold, prev_foldy)
            prev_foldy = fold[1]

    for x in range(6):
        s = ""
        for y in range(40):
            s += arr[x][y]
        print(s)


def main():
    # part1()
    part2()


if __name__ == "__main__":
    main()
