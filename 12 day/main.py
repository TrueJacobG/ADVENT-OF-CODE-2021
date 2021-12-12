from collections import defaultdict


def path(graph, node="start", visited=[], double=0):
    if node == "end":
        return 1
    if node.islower() and node in visited:
        if double == 1:
            return 0
        double += 1
    return sum(path(graph, n, visited + [node], double) for n in graph[node])


def part1():
    with open("input.txt", "r") as f:
        arr = [line.split("-") for line in f.read().splitlines()]

    graph = defaultdict(list)
    for a, b in arr:
        if b != "start":
            graph[a] += [b]
        if a != "start":
            graph[b] += [a]

    print(path(graph))
    return arr


def part2():
    arr = part1()
    graph = defaultdict(list)
    for a, b in arr:
        if b != "start":
            graph[a] += [b]
        if a != "start":
            graph[b] += [a]

    print(path(graph))


def main():
    # part1()
    part2()


if __name__ == "__main__":
    main()

