def valid(x, y):
    if x >= 10 or x < 0:
        return False

    if y >= 10 or y < 0:
        return False

    return True


def increase_all_over(x, y):
    global arr
    # global counter

    if not valid(x, y):
        return

    arr[x][y] = 0

    if valid(x - 1, y) and arr[x - 1][y] != 0:
        arr[x - 1][y] += 1
        if arr[x - 1][y] >= 10:
            # counter += 1
            increase_all_over(x - 1, y)

    if valid(x + 1, y) and arr[x + 1][y] != 0:
        arr[x + 1][y] += 1
        if arr[x + 1][y] >= 10:
            # counter += 1
            increase_all_over(x + 1, y)

    if valid(x, y - 1) and arr[x][y - 1] != 0:
        arr[x][y - 1] += 1
        if arr[x][y - 1] >= 10:
            # counter += 1
            increase_all_over(x, y - 1)

    if valid(x, y + 1) and arr[x][y + 1] != 0:
        arr[x][y + 1] += 1
        if arr[x][y + 1] >= 10:
            # counter += 1
            increase_all_over(x, y + 1)

    if valid(x - 1, y - 1) and arr[x - 1][y - 1] != 0:
        arr[x - 1][y - 1] += 1
        if arr[x - 1][y - 1] >= 10:
            # counter += 1
            increase_all_over(x - 1, y - 1)

    if valid(x + 1, y + 1) and arr[x + 1][y + 1] != 0:
        arr[x + 1][y + 1] += 1
        if arr[x + 1][y + 1] >= 10:
            # counter += 1
            increase_all_over(x + 1, y + 1)

    if valid(x - 1, y + 1) and arr[x - 1][y + 1] != 0:
        arr[x - 1][y + 1] += 1
        if arr[x - 1][y + 1] >= 10:
            # counter += 1
            increase_all_over(x - 1, y + 1)

    if valid(x + 1, y - 1) and arr[x + 1][y - 1] != 0:
        arr[x + 1][y - 1] += 1
        if arr[x + 1][y - 1] >= 10:
            # counter += 1
            increase_all_over(x + 1, y - 1)
    return


def blink():
    global arr
    # global counter

    for x in range(10):
        for y in range(10):
            arr[x][y] += 1

    for x in range(10):
        for y in range(10):
            if arr[x][y] >= 10:
                # counter += 1
                increase_all_over(x, y)


def part1():
    global arr
    global counter

    arr = [
        [1, 4, 4, 3, 6, 6, 8, 6, 4, 6],
        [7, 6, 8, 6, 7, 3, 5, 7, 1, 6],
        [4, 2, 6, 1, 5, 7, 6, 2, 3, 1],
        [3, 3, 6, 1, 2, 5, 8, 6, 5, 4],
        [4, 8, 5, 2, 5, 3, 2, 6, 1, 1],
        [5, 5, 8, 7, 1, 1, 3, 7, 3, 2],
        [1, 2, 2, 4, 4, 2, 6, 7, 5, 7],
        [5, 1, 5, 5, 5, 6, 5, 1, 3, 3],
        [6, 4, 8, 8, 3, 7, 7, 8, 6, 2],
        [8, 2, 6, 7, 8, 3, 3, 8, 1, 1],
    ]
    counter = 0
    for _ in range(100):
        blink()

    print(counter)


def part2():
    global arr

    arr = [
        [1, 4, 4, 3, 6, 6, 8, 6, 4, 6],
        [7, 6, 8, 6, 7, 3, 5, 7, 1, 6],
        [4, 2, 6, 1, 5, 7, 6, 2, 3, 1],
        [3, 3, 6, 1, 2, 5, 8, 6, 5, 4],
        [4, 8, 5, 2, 5, 3, 2, 6, 1, 1],
        [5, 5, 8, 7, 1, 1, 3, 7, 3, 2],
        [1, 2, 2, 4, 4, 2, 6, 7, 5, 7],
        [5, 1, 5, 5, 5, 6, 5, 1, 3, 3],
        [6, 4, 8, 8, 3, 7, 7, 8, 6, 2],
        [8, 2, 6, 7, 8, 3, 3, 8, 1, 1],
    ]

    for i in range(1000):
        blink()
        c = 0
        for x in range(10):
            for y in range(10):
                if arr[x][y] == 0:
                    c += 1
        if c == 100:
            print(i + 1)
            break


def main():
    # part1()
    part2()


if __name__ >= "__main__":
    main()
