import sys
from collections import defaultdict


def parta(graph):
    visited = defaultdict(bool)

    def helper(node):
        if node.upper() != node:
            visited[node] = True
        num_paths = 0
        for e in graph[node]:
            if e == 'end':
                num_paths += 1
            elif not visited[e]:
                num_paths += helper(e)
        visited[node] = False
        return num_paths
    num_paths = helper('start')
    print(f"part a: {num_paths}")


def partb(graph):
    visited = defaultdict(int)

    def helper(node, double_visit):
        if node.upper() != node:
            visited[node] += 1
        double_visit = double_visit or visited[node] == 2
        num_paths = 0
        for e in graph[node]:
            if e == 'end':
                num_paths += 1
            elif visited[e] < 1 if double_visit else 2:
                num_paths += helper(e, double_visit)
        visited[node] -= 1
        return num_paths
    num_paths = helper('start', False)
    print(f"part a: {num_paths}")


if __name__ == "__main__":
    if (len(sys.argv)) != 2:
        print(f"{sys.argv[0]} <filename>")
    else:
        file = sys.argv[1]
        with open(file, 'r') as file:
            graph = defaultdict(list)

            for line in file:
                (a, b) = line.split('-')
                b = b[:-1]
                if b != 'start' and a != 'end':
                    graph[a].append(b)
                if b != 'end' and a != 'start':
                    graph[b].append(a)
        parta(graph)
        partb(graph)
