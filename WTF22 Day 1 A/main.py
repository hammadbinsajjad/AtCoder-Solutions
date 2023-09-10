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
    n, m, a, b = inp_map(int)
    x = inp_list(int)
    mx = max(0, n - a + b)
    count = [0] * n
    for el in x:
        count[el - 1] += 1
    count.sort()
    saved = 0
    for el in count:
        if el <= b:
            b -= el
            saved += 1
        mx = max(saved, mx)
    print(mx)

def main():
    t = 1
    for _ in range(t):
        solve()

def input():
    return sys.stdin.readline().strip('\r\n')

def inp_int():
    return int(input())

def inp_map(f=None):
    return map(f, input().split()) if f else map(int, input().split())

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