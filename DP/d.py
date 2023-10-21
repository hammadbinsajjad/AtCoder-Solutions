import sys
import operator as op

def input():
    return sys.stdin.readline().strip("\r\n")

def main():
    n, w = map(int, input().split())
    items = [{}] * n

    for i in range(n):
        _w, _v = map(int, input().split())
        items[i] = {"w" : _w, "v" : _v}

    items.sort(key=op.itemgetter("w"))

    dp = [[0] * (w + 1) for _ in range(n)]

    for i in range(1, w + 1):
        if i >= items[0]["w"]:
            dp[0][i] = items[0]["v"]

    for i in range(1, n):
        for j in range(1, w + 1):
            if j < items[i]["w"]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(
                    dp[i - 1][j],
                    items[i]["v"] + dp[i - 1][j - items[i]["w"]],
                    )

    print(dp[-1][-1])

main()
