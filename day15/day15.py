import sys
import heapq


def parta(grid):
    ny = len(grid)
    nx = len(grid[0])
    nodes = [(0, 0, 0)]
    distances = {}
    while True:
        val, x, y = heapq.heappop(nodes)
        if (x, y) in distances:
            continue
        distances[(x, y)] = val
        if x == nx - 1 and y == ny - 1:
            break
        if x - 1 >= 0:
            new_val = val + grid[y][x - 1]
            heapq.heappush(nodes, (new_val, x - 1, y))
        if y - 1 >= 0:
            new_val = val + grid[y - 1][x]
            heapq.heappush(nodes, (new_val, x, y - 1))
        if x + 1 < nx:
            new_val = val + grid[y][x + 1]
            heapq.heappush(nodes, (new_val, x + 1, y))
        if y + 1 < ny:
            new_val = val + grid[y + 1][x]
            heapq.heappush(nodes, (new_val, x, y + 1))
    print(f"part a: {distances[(nx-1, ny-1)]}")


def partb(grid):
    ny = len(grid)
    nx = len(grid[0])
    nodes = [(0, 0, 0)]
    distances = {}

    def maybe_add(x, y, val):
        if x >= 0 and x < 5 * nx and y >= 0 and y < 5 * ny:
            new_val = val + (grid[y % ny][x % ny] + x // nx + y // ny - 1) % 9 + 1
            heapq.heappush(nodes, (new_val, x, y))

    while True:
        val, x, y = heapq.heappop(nodes)
        if (x, y) in distances:
            continue
        distances[(x, y)] = val
        if x == 5 * nx - 1 and y == 5 * ny - 1:
            break
        maybe_add(x - 1, y, val)
        maybe_add(x + 1, y, val)
        maybe_add(x, y - 1, val)
        maybe_add(x, y + 1, val)
    print(f"part b: {distances[(5 * nx-1, 5 * ny-1)]}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"python {sys.argv[0]} <filename>")
    else:
        with open(sys.argv[1], "r") as file:
            grid = [[int(c) for c in line[:-1]] for line in file]
        parta(grid)
        partb(grid)
