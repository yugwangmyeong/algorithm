# https://www.acmicpc.net/problem/7576

from collections import deque
import sys
input = sys.stdin.readline

# bfs기본 문제
m,n = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

# 방향 벡터
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def BFS(grid):
    n = len(grid)
    m = len(grid[0])
    
    q = deque()
    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                q.append((i,j))
                
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                grid[nx][ny] = grid[x][y] + 1
                q.append((nx,ny))
BFS(grid)


days = 0
for row in grid:
    for v in row:
        if v == 0:
            print(-1)
            sys.exit()
        
    days =max(days,max(row))
    
print(days-1)