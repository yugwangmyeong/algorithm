
import sys
input = sys.stdin.readline

def DFS(x,y,grid,visted,m,n):
    # 방향벡터 x,y
    dx = [-1,1,0,0]  
    dy = [0,0,1,-1]
    
    #그 x,y의 위치가 배추라고 가정하고 dfs를 하는거니까 True인거아닌가?
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and grid [nx][ny] == 1:
            DFS(nx,ny,grid,visted,m,n)
        




t = int(input())
for _ in range(t):
    m,n,k = map(int,input().split())  # m 가로 , n 세로, k는 배추의 개수
    grid = [[0]*m for _ in range(n)]  # n*m 배추 밭 크기
    visited = [[False]*m for _ in range(n)]
    
    for _ in range(k):
        x,y = map(int,input().split()) # x,y 행열
        grid[y][x] = 1
    
    # 연결된 배추 그룹 개수 찾기
    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and visited[i][j] == False:
                DFS(i,j,grid,visited,m,n)
                count += 1

print(count)
