import sys


def parta(input):
    start = {'(', '[', '{', '<'}
    close = {')': ('(', 3), ']': ('[', 57), '}': ('{', 1197), '>': ('<', 25137)}

    def score(line):
        parens = []
        for c in line[:-1]:
            if c in start:
                parens.append(c)
            else:
                (d, v) = close[c]
                p = parens.pop()
                if d != p:
                    return v
        return 0

    with open(input, 'r') as file:
        x = 0
        for line in file:
            x += score(line)
        print(f"part a: {x}")


def partb(input):
    start = {'(', '[', '{', '<'}
    close = {')': ('(', 3), ']': ('[', 57), '}': ('{', 1197), '>': ('<', 25137)}
    vals = {'(': 1, '[': 2, '{': 3, '<': 4}

    def score(line):
        parens = []
        for c in line[:-1]:
            if c in start:
                parens.append(c)
            else:
                (d, v) = close[c]
                p = parens.pop()
                if d != p:
                    return 0
        x = 0
        for p in parens[::-1]:
            x = 5 * x + vals[p]
        return x

    with open(input, 'r') as file:
        x = sorted([s for line in file if (s := score(line)) > 0])
        print(f"part a: {x[len(x) // 2]}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{sys.argv[0]} <file>")
    else:
        input = sys.argv[1]
        parta(input)
        input = sys.argv[1]
        partb(input)
