import sys

def input():
    return sys.stdin.readline().strip()

def solve():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))

    dp = [1e9] * (n)
    dp[0] = 0

    for i in range(1, n):
        for j in range(1, k + 1):
            if i - j >= 0:
                dp[i] = min(dp[i], dp[i - j] + abs(a[i] - a[i - j]))
    print(dp[-1])

solve()
