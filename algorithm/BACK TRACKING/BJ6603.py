import sys
input = sys.stdin.readline

def recur(start,depth):
    if depth == 6:
        print(' '.join(map(str,result)))
        return
    for i in range(start,len(nums)):
        result.append(nums[i])
        recur(i+1,depth + 1)
        result.pop()
    
while True:
    line = list(map(int,input().split()))
    if line[0] == 0:
        break
    k = line[0]
    nums = line[1:]
    result = []
    recur(0,0)
    print()
        