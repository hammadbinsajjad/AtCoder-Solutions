import sys

def input():
    return sys.stdin.readline().strip()

def inp_list(f=None):
    return list(map(f, input().split())) if f else list(input())

def main():
    h, w = inp_list(int)
    graph = [[] for _ in range(h)]

    for i in range(h):
        graph[i] = inp_list()

    dp = [[0] * w for _ in range(h)]
    dp[0][0] = 1

    def inB(x, y):
        if 0 <= x < h and 0 <= y < w:
            return True
        else:
            return False

    for i in range(h):
        for j in range(w):
            if graph[i][j] == '#':
                continue

            if inB(i, j + 1) and graph[i][j + 1] != '#':
                dp[i][j + 1] = (dp[i][j + 1] + dp[i][j]) % (1e9 + 7)
            if inB(i + 1, j) and graph[i + 1][j] != '#':
                dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % (1e9 + 7)

    print(int(dp[-1][-1] % (1e9 + 7)))

main()
