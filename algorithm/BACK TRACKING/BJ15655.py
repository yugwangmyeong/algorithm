import sys
input = sys.stdin.readline

N,M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()

rs = []
used = [False]*N

def recur(start):
    if len(rs)==M:
        print(' '.join(map(str,rs)))
        return
    for i in range(N):
        if used[i]:
            continue
        if rs and rs[-1] > nums[i]:
            continue
        used[i]=True
        rs.append(nums[i])
        recur(i+1)
        rs.pop()
        used[i]=False
        
recur(0)
