#template

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
nums = list[map(int,input().split())]

def recur():
    if len(rs) == M:
        print(' '.join(map(str,rs)))
        break
    for i in range(N):