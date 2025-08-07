import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

rs = []

used = [False] * N


def recur():
    if len(rs) == M:
        print(" ".join(map(str, rs)))
        return

    prev = -1
    for i in range(N):
        if used[i]:
            continue
        if prev == nums[i]:
            continue
        used[i] = True
        rs.append(nums[i])
        recur()
        rs.pop()
        used[i] = False
        prev = nums[i]


recur()
