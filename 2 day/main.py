def part1():
    with open("input.txt", "r") as f:
        forward = 0
        depth = 0
        for x in f.readlines():
            direction, length = x.split()
            if direction == "forward":
                forward += int(length)
                continue
            if direction == "down":
                depth += int(length)
                continue
            if direction == "up":
                depth -= int(length)

    print(depth * forward)


def part2():
    with open("input.txt", "r") as f:
        horizontal = 0
        depth = 0
        aim = 0
        for x in f.readlines():
            direction, length = x.split()
            if direction == "forward":
                horizontal += int(length)
                depth += int(length) * aim
                continue
            if direction == "down":
                aim += int(length)
                continue
            if direction == "up":
                aim -= int(length)

    print(horizontal * depth)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
