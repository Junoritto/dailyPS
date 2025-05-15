import sys
input = sys.stdin.readline

N, M = map(int,input().split())
moneyList = []
for i in range(N):
    money = int(input())
    moneyList.append(money)

left = max(moneyList)
right = 1000000000

while (left<right):
    mid = (left+right)//2
    temp = 0
    cnt = 1
    for i in range(len(moneyList)):
        temp += moneyList[i]
        if temp > mid:
            temp = moneyList[i]
            cnt += 1
    if cnt <= M:
        right = mid
    else:
        left = mid + 1

print(left)
