import sys
import math
import heapq as hq

# Dijkstra Algorithm (both n^2 variant and n log n variant will work)

def input():
    return sys.stdin.readline().strip()

to_debug = False
def main():
    n, a, b, c = map(int, input().split())

    graph = [[] for _ in range(n)]

    for i in range(n):
        graph[i] = list(map(int, input().split()))

    graph_car = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            graph_car[i][j] = graph[i][j] * a

    dist_car = dijkstra(graph_car, 0)
    debug(dist_car)

    graph_bus = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            graph_bus[i][j] = graph[i][j] * b + c

    dist_bus = dijkstra(graph_bus, n - 1)
    debug(dist_bus)

    res = math.inf
    for i in range(n):
        res = min(res, dist_car[i] + dist_bus[i])
    print(res)

def dijkstra(g, s):
    n = len(g)
    dist = [math.inf] * n
    visited = [False] * n

    dist[s] = 0

    for i in range(n):
        min_val = math.inf
        cur = None
        for i, e in enumerate(dist):
            if e < min_val and not visited[i]:
                min_val = e
                cur = i

        visited[cur] = True

        for ch in range(n):
            if dist[ch] > (dist[cur] + g[cur][ch]):
                dist[ch] = dist[cur] + g[cur][ch]

    return dist

def debug(*x, end="\n", sep=" "):
    if not to_debug:
        return
    w = sys.stderr.write
    for e in x:
        w(str(e))
        w(sep)
    w(end)


main()
