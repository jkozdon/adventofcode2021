import sys
from collections import Counter, defaultdict


def parta(update, pairs):
    def imprint(pattern, pairs):
        update = ""
        for k in range(len(pattern) - 1):
            update += pattern[k]
            v = pattern[k : k + 2]
            if v in pairs.keys():
                update += pairs[v]
        update += pattern[-1]
        return update

    for _ in range(10):
        update = imprint(update, pairs)
    cnt = Counter(update).most_common()
    print(f"part a: {cnt[0][-1] - cnt[-1][-1]}")


def partb(update, pairs, max_lvl):
    found = {}

    def imprint(a, b, lvl):
        if (a, b, lvl) in found.keys():
            return
        vals = defaultdict(int)
        if lvl == max_lvl:
            vals[a] += 1
            vals[b] += 1
            found[(a, b, lvl)] = vals
            return
        if a + b in pairs.keys():
            c = pairs[a + b]
            imprint(a, c, lvl + 1)
            imprint(c, b, lvl + 1)
            for k, v in found[(a, c, lvl + 1)].items():
                vals[k] += v
            for k, v in found[(c, b, lvl + 1)].items():
                vals[k] += v
            vals[c] -= 1
        else:
            vals[a] = 1
            vals[b] = 1
        found[(a, b, lvl)] = vals

    totals = defaultdict(int)
    for idx in range(len(pattern) - 1):
        imprint(pattern[idx], pattern[idx + 1], 0)
        for k, v in found[(pattern[idx], pattern[idx + 1], 0)].items():
            totals[k] += v
        if idx > 0:
            totals[pattern[idx]] -= 1
    min_val = sys.maxsize
    max_val = 0
    for _, v in totals.items():
        min_val = min(v, min_val)
        max_val = max(v, max_val)
    print(f"part b: {max_val - min_val}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"python {sys.argv[0]} <filename>")
    else:
        with open(sys.argv[1], "r") as file:
            pattern = file.readline()[:-1]
            file.readline()
            pairs = {v[0:2]: v[-2:-1] for v in file}
    parta(pattern, pairs)
    partb(pattern, pairs, 40)
