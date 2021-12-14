def parse():
    arr = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            arr.append(line.strip("\n").split(" -> "))

    return arr


def part1():
    arr = parse()
    s = list("VHCKBFOVCHHKOHBPNCKO")

    for x in range(40):
        print(x)
        i = 1
        while i < len(s):
            check = f"{s[i-1]}{s[i]}"
            for pair in arr:
                if pair[0] == check:
                    s.insert(i, pair[1])
                    i += 1
                    break
            i += 1

    without_repeating = list(set(s))
    # dct = dict()
    # for letter in without_repeating:
    #     dct[letter] = s.count(letter)
    results = []
    for letter in without_repeating:
        results.append(s.count(letter))

    print(max(results) - min(results))


def main():
    part1()


if __name__ == "__main__":
    main()
