import sys
input = sys.stdin.readline

N,M = map(int,input().split())
rs = []

def recur(num):
    if len(rs) == M:
        print(' '.join(map(str,rs)))
        return
    for i in range(num,N+1):
        rs.append(i)
        recur(i)
        rs.pop()
recur(1)