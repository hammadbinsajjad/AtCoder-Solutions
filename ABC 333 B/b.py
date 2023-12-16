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
    s1, s2 = list(input())
    t1, t2 = list(input())

    if bfs(s1, s2) == bfs(t1, t2):
        print("Yes")
    else:
        print("No")

graph = {
    'A': ['E', 'B'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'E'],
    'E': ['D', 'A']
}

def bfs(s, e):
    q = clc.deque()
    push = q.append
    pop = q.popleft

    visited = set()

    push((s, 0))

    while q:
        c, d = pop()

        if c == e:
            return d

        for ch in graph[c]:
            if ch not in visited:
                push((ch, d + 1))
        


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