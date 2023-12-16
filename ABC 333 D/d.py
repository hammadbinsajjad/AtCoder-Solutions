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

    graph = [[] for  _ in range(n)]

    for _ in range(n - 1):
        a, b = inp_map(int)
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    res = []
    for ch in graph[0]:
        v = dfs(graph, ch)
        res.append(v)

    res.sort()
    res.pop()

    print(sum(res) + 1)

def dfs(g, s):
    stack = []
    push = stack.append
    pop = stack.pop

    push(s)

    visited = set([s, 0])

    while stack:
        c = pop()
        
        for ch in g[c]:
            if ch not in visited:
                push(ch)
                visited.add(ch)

    return len(visited) - 1

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