import sys
import re
from collections import defaultdict


def parta(vals):
    v = vals[2] * (vals[2] + 1) // 2
    print(f"Part a: {v}")


def partb(vals):
    xmin, xmax, ymin, ymax = vals
    y_in = defaultdict(set)
    for vy0 in range(ymin, -ymin):
        y = 0
        vy = vy0
        t = 0
        t_max = 0
        while y > ymin:
            y += vy
            t += 1
            vy -= 1
            if ymin <= y <= ymax:
                y_in[t].add(vy0)
                t_max = max(t, t_max)

    found = set()
    for vx0 in range(0, xmax + 1):
        vx = vx0
        t = 0
        x = 0
        while vx > 0:
            if xmin <= x <= xmax:
                for vy0 in y_in[t]:
                    found.add((vx0, vy0))
            x += vx
            t += 1
            vx -= 1
        if xmin <= x <= xmax:
            for t in range(t, t_max + 1):
                for vy0 in y_in[t]:
                    found.add((vx0, vy0))
    print(f"Part b: {len(found)}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"python {sys.argv[0]} <filename>")
    else:
        with open(sys.argv[1], "r") as file:
            string = file.readline()
            vals = [int(v) for v in re.findall(r"-?\d+", string)]
        parta(vals)
        partb(vals)
