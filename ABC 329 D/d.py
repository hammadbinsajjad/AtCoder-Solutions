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
    n, m = inp_map(int)
    a = inp_list(int)

    pq = []

    push = lambda x: hq.heappush(pq, x)
    pop = lambda x: hq.heappop(pq)

    count = [0] * (n + 1)

    for e in a:
        count[e] += 1
        # debug(e, pq)
        push((-count[e], e))
        print(pq[0][1])

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