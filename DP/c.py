import sys
def input():
    return sys.stdin.readline().strip("\r\n")
def inp_list(f):
    return list(map(f, input().split()))

def solve():
    n = int(input())
    a, b, c = inp_list(int)

    for _ in range(n - 1):
        x, y, z = inp_list(int)

        ta, tb, tc = a, b, c
        a = max(x + tb, x + tc)
        b = max(y + ta, y + tc)
        c = max(z + ta, z + tb)
    print(max(a, b, c))

solve()
