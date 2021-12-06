import numpy as np


def how_many_fishes(day):
    with open("input.txt", "r") as file:
        c = np.fromiter(
            (int(value) for value in file.readline().split(",")), dtype="int8"
        )

    fishes = np.fromiter((np.count_nonzero(c == i) for i in range(7)), dtype="uint64")
    cooldown = np.zeros(2)

    for _ in range(day):
        fishes = np.roll(fishes, -1)
        cooldown = np.roll(cooldown, -1)
        new_fishes = fishes[-1]
        cooldown_finished = cooldown[-1]
        fishes[-1] += cooldown_finished
        cooldown[-1] = new_fishes

    return np.sum(fishes) + np.sum(cooldown)


def main():
    print(how_many_fishes(80))
    print(how_many_fishes(256))


if __name__ == "__main__":
    main()
