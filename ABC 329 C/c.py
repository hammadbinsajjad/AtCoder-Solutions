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
    s = list(input().strip())
    s.append("-")

    count = [0] * 26
    count[ord(s[0]) - 97] = 1

    l = 0
    for r in range(n + 1):
        if s[r] == s[l]:
            continue
        else:
            count[ord(s[l]) - 97] = max(count[ord(s[l]) - 97], r - l if r != l else 1)
            l = r
    print(sum(count)) 

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