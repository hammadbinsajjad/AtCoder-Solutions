import sys

def input():
    return sys.stdin.readline().strip()

def main():
    h, w = map(int, input().split())

    graph = [[""]*w for _ in range(h)]

    for i in range(h):
        graph[i] = list(input())

    res = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '#':
                res += 1
                dfs(graph, (i,j))
    print(res)

visited = set()
def dfs(g, n):
    stack = []
    push = stack.append
    pop = stack.pop

    push(n)

    while stack:
        cur = pop()
        x, y = cur
        inBounds = lambda x, y, g: 0 <= x < len(g) and 0 <= y < len(g[0])

        if not inBounds(x, y, g) or g[x][y] == '.':
            continue 

        g[x][y] = "."

        for i in (1, -1):
            push((x + i, y))
            push((x, y + i))
            push((x + i, y + i))
        
        push((x + 1, y - 1))
        push((x - 1, y + 1))

main() 