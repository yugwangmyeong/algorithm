import sys

# deque함수 호출
from collections import deque

input = sys.stdin.readline

# n,m 2차원 배열만들기 띄어쓰기있으려면 split(), 그냥 붙이려면 strip()6
n, m = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(n)]

# 방향벡터설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS():
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    queue.append((0, 0, 1))
    visited[0][0] = True

    while queue:
        y, x, distance = queue.popleft()

        if y == n - 1 and x == m - 1:
            return distance
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:  # 경계안에서
                if grid[ny][nx] == 1:  # 갈수있는 곳이 1인지 확인
                    if not visited[ny][nx]:
                        visited[ny][nx] = True
                        queue.append((ny, nx, distance + 1))


print(BFS())
