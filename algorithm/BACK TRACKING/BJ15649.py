"""
1. 아이디어 1부터 N중에 하나 선택한뒤
다음 1부터 N부터 선택할때 이미 선택한 갓ㅂ이 아닌경우 선택
M개를 선택할 경우 프린트

2. 시간 복잡도 N^N: 중복이 가능, N=8까지 가능
   N! : 중복잉 불가, N = 10까지 가능
   
3. 방문 여부 확인 배열: bool[]
   선택한 값 입력 배열: int[]  
"""

import sys
input = sys.stdin.readline

N, M = map(int,input().split())
rs = []
chk = [False] * (N+1)

def recur(num):
    if num == M:
        print(' '.join(map(str,rs)))
        return
    for i in range(1, N+1):
        if chk[i] == False:
            chk[i] = True
            rs.append(i)
            recur(num+1)
            chk[i] = False
            rs.pop()
            
recur(0)

