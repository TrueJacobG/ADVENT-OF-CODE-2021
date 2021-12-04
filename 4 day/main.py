def get_boards():
    boards = []

    with open("input.txt", "r") as f:
        board = []
        for line in f.readlines():
            if line.strip("\n") == "":
                boards.append(board)
                board = []
                continue

            verse = []
            for element in line.strip("\n").split(" "):
                if element != "":
                    verse.append([int(element), False])

            board.append(verse)

    return boards


def sum_of_unmarked(board):
    s = 0
    for l in range(len(board)):
        for e in board[l]:
            if not e[1]:
                s += e[0]
    return s


def check_boards(boards):
    for y in range(0, len(boards)):
        for l in range(len(boards[y])):
            counter = 0
            for e in range(len(boards[y][l])):
                if boards[y][l][e][1]:
                    counter += 1
            if counter == len(boards[y][l]):
                return sum_of_unmarked(boards[y])

        for e in range(5):
            counter = 0
            for l in range(5):
                if boards[y][l][e][1]:
                    counter += 1
            if counter == 5:
                return sum_of_unmarked(boards[y])

    return 0


def check_board(board):
    for l in range(len(board)):
        counter = 0
        for e in range(len(board[l])):
            if board[l][e][1]:
                counter += 1
        if counter == len(board[l]):
            return 1

        for e in range(5):
            counter = 0
            for l in range(5):
                if board[l][e][1]:
                    counter += 1
            if counter == 5:
                return 1
    return 0


def check_boards2(boards):
    c = 0
    for y in range(0, len(boards)):
        c += check_board(boards[y])

    return c


def last_board(boards):
    for y in range(0, len(boards)):
        flag = True
        for l in range(len(boards[y])):
            counter = 0
            for e in range(len(boards[y][l])):
                if boards[y][l][e][1]:
                    counter += 1
            if counter == len(boards[y][l]):
                flag = False

        for e in range(5):
            counter = 0
            for l in range(5):
                if boards[y][l][e][1]:
                    counter += 1
            if counter == 5:
                flag = False

        if flag:
            return y


def get_numbers():
    numbers = [
        83,
        5,
        71,
        61,
        88,
        55,
        95,
        6,
        0,
        97,
        20,
        16,
        27,
        7,
        79,
        25,
        81,
        29,
        22,
        52,
        43,
        21,
        53,
        59,
        99,
        18,
        35,
        96,
        51,
        93,
        14,
        77,
        15,
        3,
        57,
        28,
        58,
        17,
        50,
        32,
        74,
        63,
        76,
        84,
        65,
        9,
        62,
        67,
        48,
        12,
        8,
        68,
        31,
        19,
        36,
        85,
        98,
        30,
        91,
        89,
        66,
        80,
        75,
        47,
        4,
        23,
        60,
        70,
        87,
        90,
        13,
        38,
        56,
        34,
        46,
        24,
        41,
        92,
        37,
        49,
        73,
        10,
        94,
        26,
        42,
        40,
        33,
        54,
        86,
        82,
        72,
        39,
        2,
        45,
        78,
        11,
        1,
        44,
        69,
        64,
    ]
    return numbers


def part1():
    numbers = get_numbers()
    boards = get_boards()

    for x in range(0, len(numbers)):
        for y in range(0, len(boards)):
            for l in range(len(boards[y])):
                for e in range(len(boards[y][l])):
                    if numbers[x] == boards[y][l][e][0]:
                        boards[y][l][e] = [boards[y][l][e][0], True]
        s = check_boards(boards)
        if s != 0:
            return s * numbers[x]


def part2():
    numbers = get_numbers()
    boards = get_boards()

    for x in range(0, len(numbers)):
        for y in range(0, len(boards)):
            for l in range(len(boards[y])):
                for e in range(len(boards[y][l])):
                    if numbers[x] == boards[y][l][e][0]:
                        boards[y][l][e] = [boards[y][l][e][0], True]
        c = check_boards2(boards)
        if c == len(boards) - 1:
            for line in boards[last_board(boards)]:
                print(line)
            print("next -> ", numbers[x + 1])


def main():
    print(part1())
    print(part2())


if __name__ == "__main__":
    main()
