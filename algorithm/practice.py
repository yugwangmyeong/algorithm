import sys
input = sys.stdin.readline

N = input(int,input().strip())
grid = [list(map(int,input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]



