import sys
input = sys.stdin.readline

N,M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort() # 정렬

rs = []
used = [False] * N  # 일단 배열들 False로 설정


def recur():
    if len(rs)==M:
        print(' '.join(map(str,rs)))
        return
    for i in range(N):
        if not used[i]:
            used[i]= True # i번째 배열 True로 설정
            rs.append(nums[i]) # # nums i번째 추가
            recur()  # 다시 재호출
            rs.pop() # 했으니까 다시 제거
            used[i] = False

recur()