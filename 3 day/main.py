def part1():
    counter = []
    for i in range(13):
        counter.append(0)

    with open("input.txt", "r") as f:
        for x in f.readlines():
            for i, bit in enumerate(x):
                if bit == "1":
                    counter[i] += 1
                elif bit == "0":
                    counter[i] -= 1

    gamma = ""
    for x in counter:
        if x > 0:
            gamma += "1"
        else:
            gamma += "0"

    gamma = gamma[:-1]

    epsilon = "".join(["1" if x == "0" else "0" for x in gamma])

    print(gamma)
    print(epsilon)
    print(int(gamma, 2) * int(epsilon, 2))


def part2():
    numbers = []
    with open("input.txt", "r") as f:
        for x in f.readlines():
            numbers.append(x.strip("\n"))

    numbers2 = list(numbers)

    i = 0
    for x in range(12):
        if len(numbers) == 1:
            break

        the_most_common = 0

        for el in numbers:
            if el[i] == "1":
                the_most_common += 1
            else:
                the_most_common -= 1

        if the_most_common >= 0:
            numbers = filter(lambda x: x[i] == "1", numbers)
        else:
            numbers = filter(lambda x: x[i] == "0", numbers)

        i += 1

    print(numbers)

    i = 0
    for x in range(12):
        if len(numbers2) == 1:
            break

        the_least_common = 0

        for el in numbers2:
            if el[i] == "1":
                the_least_common += 1
            else:
                the_least_common -= 1

        if the_least_common < 0:
            numbers2 = filter(lambda x: x[i] == "1", numbers2)
        else:
            numbers2 = filter(lambda x: x[i] == "0", numbers2)

        i += 1

    print(numbers2)

    print(int(numbers[0], 2) * int(numbers2[0], 2))


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
