import sys
input = sys.stdin.readline

n,m = map(int, input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]


from collections import deque
queue = deque()

print(grid)
