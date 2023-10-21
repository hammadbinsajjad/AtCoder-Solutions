import sys

def input():
    return sys.stdin.readline().strip()

def checkRemoved(s, t):
    u = 0 # s
    d = 0 # t

    diff = False
    for i in range(len(t)):
        if i == len(t) - 1 and not diff:
            break
        if t[d] == s[u]:
            u += 1
            d += 1
        else:
            d += 1
            if diff:
                return False
            else:
                diff = True
    return True

def checkDiff(s, t):
    u = 0
    d = 0

    diff = False
    for _ in range(len(t)):
        if s[u] != t[d]:
            if diff:
                return False
            else:
                diff = True
        u += 1
        d += 1
    return True

def solve():
    n, t = input().split()
    n = int(n)

    res = []

    done = False
    for i in range(n):
        _s = input()
        if abs(len(_s) - len(t)) > 1:
            continue
        if len(_s) == len(t):
            if _s == t:
                res.append(i + 1)
                done = True
            else:
                if checkDiff(_s, t):
                    res.append(i + 1)
                    done = True
        elif len(_s) < len(t):
            if checkRemoved(_s, t):
                res.append(i + 1)
                done = True
        elif len(_s) > len(t):
            if checkRemoved(t, _s):
                res.append(i + 1)
                done = True
    
    if not done:
        print(0)
    else:
        print(len(res))
        for e in res:
            print(e, end=" ")

        print()
solve()