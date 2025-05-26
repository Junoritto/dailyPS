import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

left = 0
right = 0
answer = 0
fruit_count = defaultdict(int)
type_count = 0

while right<N:
    fruit_count[arr[right]] += 1
    if fruit_count[arr[right]] == 1: # 새로운 종류의 과일이면
        type_count += 1
    
    # 과일 종류가 2를 초과하면 왼쪽 포인터 이동
    while type_count > 2:
        fruit_count[arr[left]] -= 1
        if fruit_count[arr[left]] == 0: # 해당 종류 과일이 더 이상 없으면
            type_count -= 1
        left += 1
    
    answer = max(answer, right-left+1)
    right += 1

print(answer)