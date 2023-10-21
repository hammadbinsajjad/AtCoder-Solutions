import sys

def input():
    return sys.stdin.readline().strip()

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    dp = [1e9] * (n)
    dp[0] = 0

    for i in range(1, n):
        for j in (1, 2):
            if i - j >= 0:
                dp[i] = min(dp[i], dp[i - j] + abs(a[i] - a[i - j]))
    print(dp[-1])

solve()
