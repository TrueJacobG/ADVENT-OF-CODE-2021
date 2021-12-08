def part1():
    codes = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            codes.append(line[line.index("|") + 2 :].strip("\n"))

    result = 0

    for code in codes:
        for word in code.split(" "):
            length = len(word)
            if length == 7 or length == 2 or length == 3 or length == 4:
                result += 1

    print(result)
    return codes


def get_symbols(words1, words2):
    words = sorted(words1 + words2, key=len)

    print(words)

    symbols = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
    }
    for word in words:
        if len(word) == 2:
            for letter in list(word):
                if letter not in symbols[2]:
                    symbols[2].append(letter)
                if letter not in symbols[5]:
                    symbols[5].append(letter)

        if len(word) == 3:
            for letter in list(word):
                if (
                    letter not in symbols[2]
                    and letter not in symbols[5]
                    and letter not in symbols[0]
                ):
                    symbols[0].append(letter)

        if len(word) == 4:
            for letter in list(word):
                if (
                    letter not in symbols[2]
                    and letter not in symbols[5]
                    and letter not in symbols[1]
                ):
                    if len(symbols[1]) != 1:
                        symbols[1].append(letter)

                if (
                    letter not in symbols[2]
                    and letter not in symbols[5]
                    and letter not in symbols[3]
                ):
                    symbols[3].append(letter)

        if len(word) == 7:
            pass

        if len(word) == 5:
            if (
                (symbols[2][0] in word or symbols[2][1] in word)
                and (symbols[3][0] in word or symbols[3][1] in word)
                and symbols[0][0] in word
            ):
                for letter in list(word):
                    if len(symbols[4]) != 1:
                        if (
                            letter not in symbols[2]
                            and letter not in symbols[3]
                            and letter not in symbols[0]
                            and letter not in symbols[4]
                        ):
                            symbols[4].append(letter)

                    if len(symbols[6]) != 1:
                        if (
                            letter not in symbols[2]
                            and letter not in symbols[3]
                            and letter not in symbols[0]
                        ):
                            symbols[6].append(letter)

            if (
                (symbols[3][0] in word or symbols[3][1] in word)
                and symbols[0][0] in word
                and symbols[2][0] in word
                and symbols[2][1] in word
            ):
                for letter in list(word):
                    if (
                        letter not in symbols[0]
                        and letter not in symbols[2]
                        and letter not in symbols[3]
                        and letter not in symbols[5]
                    ):
                        symbols[6] = [letter]

            if (
                symbols[0][0] in word
                and symbols[6][0] in word
                and (symbols[5][0] in word or symbols[5][1] in word)
                and (symbols[3][0] in word or symbols[3][1] in word)
            ):
                for letter in list(word):
                    if (
                        letter not in symbols[0]
                        and letter not in symbols[6]
                        and letter not in symbols[5]
                        and letter not in symbols[3]
                    ):
                        print(letter)
                        symbols[1] = [letter]
                        symbols[4] = [x for x in symbols[4] if x != letter]

            if (
                symbols[0][0] in word
                and (symbols[2][0] in word or symbols[2][1] in word)
                and letter not in symbols[4]
                and letter not in symbols[6]
            ):
                # symbols[2] = [letter]
                # symbols[5] = [x for x in symbols[5] if x != letter]
                pass
    print(symbols)


def part2():
    codes = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            words = []
            words.append(line[: line.index("|") - 1].strip("\n"))
            words.append(line[line.index("|") + 2 :].strip("\n"))
            codes.append(words)

    for code in codes:
        words1 = code[0].split(" ")
        words2 = code[1].split(" ")
        symbols = get_symbols(words1, words2)
        break


def main():
    # part1()
    part2()


if __name__ == "__main__":
    main()
