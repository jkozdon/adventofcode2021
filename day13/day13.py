import sys


def fold(holes, fold):
    folded_holes = set()
    if fold[0] == 'x':
        val_x = fold[1]
        for h in holes:
            if h[0] >= val_x:
                folded_holes.add((2 * val_x - h[0], h[1]))
            else:
                folded_holes.add(h)
    elif fold[0] == 'y':
        val_y = fold[1]
        for h in holes:
            if h[1] >= val_y:
                folded_holes.add((h[0], 2 * val_y - h[1]))
            else:
                folded_holes.add(h)
    return folded_holes


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"python {sys.argv[0]} <input file>")
    else:
        with open(sys.argv[1], 'r') as file:
            holes = set()
            folds = []
            for line in file:
                val = line.split(',')
                if len(val) == 2:
                    (x, y) = (int(val[0]), int(val[1]))
                    holes.add((x, y))
                elif len(val[0]) > 1:
                    (dir, loc) = val[0][11:].split('=')
                    folds.append((dir, int(loc)))
        folded = fold(holes, folds[0])
        print(f"part a: {len(folded)}")
        print("part b")
        for f in folds[1:]:
            folded = fold(folded, f)
        locs = []
        for (x, y) in folded:
            while y > len(locs) - 1:
                locs.append([])
            while x > len(locs[y]) - 1:
                locs[y].append(" ")
            locs[y][x] = '#'
        for row in locs:
            print(''.join(row))
