import sys
import math
import bisect as bs
import string as strn
import heapq as hq
import collections as clc
import itertools as it
import operator as op
import copy as cp

to_debug = True
def solve():
    n = inp_int()
    x = [0] * n
    y = [0] * n
    z = [0] * n

    for i in range(n):
        x[i], y[i], z[i] = inp_list(int)

    sz = sum(z)

    diff = []

    obt = 0

    for i in range(n):
        if x[i] < y[i]:
            diff.append((y[i] - x[i], z[i]))
        else:
            obt += z[i]

    print(diff)
    print(sz - obt)

    if obt > math.ceil(sz/2):
        print(0)
        return

    dp = [math.inf for _ in range(sz - obt)]

    dp[0] = 0
 
def main():
    t = 1
    for _ in range(t):
        solve()

def input():
    return sys.stdin.readline().strip('\r\n')

def inp_int():
    return int(input())

def inp_list(f=None):
    return list(map(f, input().split())) if f else list(input())

def print(x='', end='\n'):
    sys.stdout.write(str(x))
    sys.stdout.write(end)

def debug(*x, end='\n', sep=' '):
    if not to_debug:
        return
    for _x in x:
        sys.stderr.write(str(_x))
        sys.stderr.write(str(sep))
    sys.stderr.write(end)

main()