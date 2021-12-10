def remove_pairs(line):
    direct_pairs = ["[]", "()", "<>", "{}"]
    while True:
        for pair in direct_pairs:
            line = line.replace(pair, "")
        if not any(direct_pair in line for direct_pair in direct_pairs):
            break
    return line


def part1():
    lines = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            lines.append(line.strip("\n"))

    without_corrupted = []
    counter = 0
    for i in range(len(lines)):
        line = remove_pairs(lines[i])
        flag = True
        for symbol in line:
            if symbol == ")":
                counter += 3
                flag = False
                break
            if symbol == "]":
                counter += 57
                flag = False
                break
            if symbol == "}":
                counter += 1197
                flag = False
                break
            if symbol == ">":
                counter += 25137
                flag = False
                break

        if flag:
            without_corrupted.append(lines[i])

    print(counter)
    return without_corrupted


def part2():
    lines = part1()

    points = {")": 1, "]": 2, "}": 3, ">": 4}
    counters = []

    for line in lines:
        counter = 0
        result = ""
        for i in range(len(line) - 1, -1, -1):
            if line[i] == "{":
                result += "}"
            if line[i] == "[":
                result += "]"
            if line[i] == "(":
                result += ")"
            if line[i] == "<":
                result += ">"

        for x in result:
            counter *= 5
            counter += points[x]

        counters.append(counter)

    counters = sorted(counters)
    print(counters[len(counters) // 2])


def main():
    # part1()
    part2()


if __name__ == "__main__":
    main()
