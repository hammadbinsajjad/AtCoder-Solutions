import sys
import math

def input():
    return sys.stdin.readline().strip()

def main():
    n, a, b, c = map(int, input().split())

    graph = [[] for _ in range(n)]

    for i in range(n):
        graph[i] = list(map(int, input().split()))

    graph_car = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            graph_car[i][j] = graph[i][j] * a


    dist_car = bellman_ford(graph_car, 0)

    graph_bus = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            graph_bus[i][j] = graph[i][j] * b + c

    dist_bus = bellman_ford(graph_bus, n - 1)

    res = math.inf
    for i in range(n):
        res = min(res, dist_bus[i] + dist_car[i])

    print(res)

def bellman_ford(g, x):
    n = len(g)
    dist = [math.inf] * n
    dist[x] = 0

    for i in range(n - 1):
        for u in range(n):
            for v in range(n):
                dist[v] = min(dist[v], dist[u] + g[u][v])

    return dist

main()
