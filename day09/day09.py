import sys
from collections import defaultdict


def parta(input):
    n = len(input)
    m = len(input[0])
    tot = 0
    for i in range(n):
        for j in range(m):
            v = input[i][j]
            if i-1 >= 0 and input[i-1][j] <= v:
                continue
            if i+1 < n and input[i+1][j] <= v:
                continue
            if j-1 >= 0 and input[i][j-1] <= v:
                continue
            if j+1 < m and input[i][j+1] <= v:
                continue
            tot += v + 1
    print(f"part a: {tot}")


def partb(input):
    n = len(input)
    m = len(input[0])
    to_visit = set()
    vals = [0,0,0]
    def check(i,j):
        if i >= 0 and i < n and j >= 0 and j < m and input[i][j] != 9:
            input[i][j] = 9
            to_visit.add((i, j))
    for i in range(n):
        for j in range(m):
            if input[i][j] != 9:
                to_visit.add((i, j))
                input[i][j] = 9
                x = 0
                while len(to_visit) != 0:
                    x += 1
                    (k, l) = to_visit.pop()
                    check(k-1, l)
                    check(k+1, l)
                    check(k, l-1)
                    check(k, l+1)
                if x > vals[0]:
                    vals = [x, vals[0], vals[1]]
                elif x > vals[1]:
                    vals = [vals[0], x, vals[1]]
                elif x > vals[2]:
                    vals = [vals[0], vals[1], x]
    print(f"part b: {vals[0] * vals[1] * vals[2]}")



if __name__ == "__main__":
    if (len(sys.argv)) != 2:
        print(f"{sys.argv[0]} <filename>")
    else:
        file = sys.argv[1]
        with open(file, 'r') as file:
            input = [[int(v) for v in w[:-1]] for w in file]
        parta(input)
        partb(input)
