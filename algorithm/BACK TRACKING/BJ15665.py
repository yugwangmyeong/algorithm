import sys
input = sys.stdin.readline

N,M = map(int,input().split())
nums = list[map(int,input().split())]

rs = []

def recur(start):
    if len(rs) == M:
        print(' '.join(map(str,rs)))
        return
    for i in range(N):
        rs.append(nums[i])
        recur(start)
        rs.pop()
        
recur(0)