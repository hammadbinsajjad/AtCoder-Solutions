import sys
import math
import bisect as bs
import string as strn
import heapq as hq
import collections as clc
import itertools as it
import operator as op
import copy as cp
import queue as q

to_debug = True
def solve():
    n = inp_int()

    b = [{} for _ in range(n)]

    for i in range(n):
        w, x = inp_map(int)
        b[i] = {"w":w, "x":x}
    # print(b)
    res = -1
    for i in range(0, 24):
        resc = 0
        for j in range(n):
            if 9 <= calcTime(b[j]["x"], i) < 18:
                resc += b[j]["w"]
        res = max(res, resc)
    print(res)

def calcTime(c, s):
    return (c + s) % 24

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