import sys
input = sys.stdin.readline

N,M = map(int,input().split())

nums = list(map(int,input().split()))
nums.sort()
rs = []

def recur(start):
    if len(rs) == M:
        print(' '.join(map(str,rs)))
        return
    for i in range(start,N):
        rs.append(nums[i])
        recur(i)
        rs.pop()

recur(0)