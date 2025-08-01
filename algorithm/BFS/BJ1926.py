"""
BFS
1. 아이디어
- 2중 for => 값 1 && 방문X => BFS
- BFS 돌면서 그림 개수 +1, 최대값 갱신 
2. 시간복잡도
- BFS : O(V+E)
- V : 500 * 500
- V+E : 5 * 250000 = 100만 < 2억
3. 자료구조
- 그래프 전체 지도 : int[][]
- 방문 : bool[][]
- Queue(BFS)
"""

import sys
input = sys.stdin.readline


n,m = map(int, input().split())

#입력받을때 map함수쓰는이유는 input입력받을때 string으로받으니까 int형으로 변형하려고 쓰는것
grid = [list(map(int, input().split())) for _ in range(n)]
#일단 2차원배열 전부 False로 설정
chk = [[False]*m for _ in range(n)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(y,x):
    rs = 1
    q = [(y,x)]
    while q:
        ey,ex = q.pop()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    rs += 1
                    chk[ny][nx] = True
                    q.append((ny,nx))
    return rs
        
        
cnt = 0
maxv = 0
for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            # 전체 그림 갯수를 +1
            cnt += 1
            # BFS > 그림 크기를 구해주고
            maxv = max(maxv,bfs(j,i))
            
print(cnt)
print(maxv)