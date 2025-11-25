import sys


def parta(input):
    n = len(input)
    m = len(input[0])

    def step(input, flashes):
        for j in range(n):
            for i in range(m):
                input[j][i] += 1
                if input[j][i] > 9:
                    flashes.add((i, j))

    count = 0
    for t in range(100):
        flashes = set()
        flashed = set()
        step(input, flashes)
        while len(flashes) > 0:
            (i, j) = flashes.pop()
            input[j][i] = 0
            flashed.add((i, j))
            count += 1
            for y in range(-1, 2):
                for x in range(-1, 2):
                    a = i + x
                    b = j + y
                    if 0 <= a < n and 0 <= b < m and (a, b) not in flashed:
                        input[b][a] += 1
                        if input[b][a] > 9:
                            flashes.add((a, b))
    print(f"part a: {count}")


def partb(input):
    n = len(input)
    m = len(input[0])

    def step(input, flashes):
        for j in range(n):
            for i in range(m):
                input[j][i] += 1
                if input[j][i] > 9:
                    flashes.add((i, j))

    count = 0
    while True:
        count += 1
        flashes = set()
        flashed = set()
        step(input, flashes)
        while len(flashes) > 0:
            (i, j) = flashes.pop()
            input[j][i] = 0
            flashed.add((i, j))
            for y in range(-1, 2):
                for x in range(-1, 2):
                    a = i + x
                    b = j + y
                    if 0 <= a < n and 0 <= b < m and (a, b) not in flashed:
                        input[b][a] += 1
                        if input[b][a] > 9:
                            flashes.add((a, b))
        if len(flashed) == n * m:
            break
    print(f"part b: {count}")
    pass


if __name__ == "__main__":
    if (len(sys.argv)) != 2:
        print(f"{sys.argv[0]} <filename>")
    else:
        file = sys.argv[1]
        with open(file, 'r') as file:
            input = [[int(v) for v in w[:-1]] for w in file]

        parta([line[:] for line in input])
        partb(input)
