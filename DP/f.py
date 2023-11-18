import sys
from math import inf

def input():
    return sys.stdin.readline().strip()

def inp_list(f):
    return list(map(f, input().split())) if f else list(input())

def main():
    s = input()
    t = input()

    dp = [[0] * (len(t)) for _ in range(len(s))]
    p = [[(0,0)]* len(t) for _ in range(len(s))]

    inB = lambda x, y: 0 <= x < len(s) and 0 <= y < len(t)

    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                if inB(i - 1, j - 1):
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1
            else:
                v1, v2 = 0, 0
                if inB(i - 1, j):
                    v1 = dp[i - 1][j]
                if inB(i, j - 1):
                    v2 = dp[i][j - 1]
                dp[i][j] = max(v1, v2)

    #for row in dp:
        #print(row)

    print(dp[-1][-1])
main()
