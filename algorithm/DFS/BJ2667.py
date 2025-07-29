"""
1.아이디어
- 2중 FOR문, 값 1 && 방문 x => DFS
- DFS 통해 찾은 값을 저장해서 후 정렬 해서 출력
2. 시간 복잡도
- DFS : O(V+E)
- V+E : 5N^2 ~= 625 
3. 자료구조
- 그래프 저장 : int[][]
- 방문여부 : bool[][]
- 결과값 : int[]
"""


import sys
input = sys.stdin.readline

N = int(input().strip())
grid = [list(map(int,input().strip())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
result = []


# dfs에서 움직여야할 방향벡터설정
# dy=[-1,1,0,0]
# dx=[0,0,1,-1]
dy = [1,-1,0,0]   # 아래 → 위 → 오른쪽 → 왼쪽
dx = [0,0,1,-1]

# dfs를 y,x로 받는이유는 보통 프로그래밍 언어에서 행 우선 순회를 따르기때문에
def DFS(y,x):
    cnt = 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < N and 0 <= nx < N:
            if grid[ny][nx] == 1 and visited[ny][nx] == False:
                visited[ny][nx] = True
                cnt += DFS(ny,nx)
    return cnt 
    
for j in range(N):
        for i in range(N):
            if grid[j][i] == 1 and visited[j][i] == False:
                visited[j][i] = True
                size = DFS(j,i)
                result.append(size)
                # 방문 체크 표시
                # DFS로 크기 구하기
                
result.sort()
print(len(result))
for i in result:
    print(i)
    

    
