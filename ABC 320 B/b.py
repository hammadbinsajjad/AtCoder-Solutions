import sys
import math
import bisect as bs
import string as strn
import heapq as hq
import collections as clc
import itertools as it
import operator as op
import copy as cp

def palindrome(s):
    l = 0
    r = len(s) - 1

    while l <= r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            return -1
    return len(s)

to_debug = False
def solve():
    s = input()
    res = 1

    for i in range(len(s)):
        for j in range(i, len(s)):
            t = palindrome(s[i:j + 1])
            # debug(i, j, t)
            res = max(t, res)
    
    print(res)

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