import sys
input = sys.stdin.readline

N = int(input())
NList = list(map(int,input().split()))
NList.sort()

ans = 0
for i in range(0,len(NList)):
    target = NList[i]
    left = 0
    right = len(NList)-1
    while (left<right):
        temp = NList[left] + NList[right]
        if temp > target:
            right-=1
        elif temp < target:
            left+=1
        else:
            if left == i:
                left += 1
            elif right == i:
                right -= 1
            else:
                ans += 1
                break

print(ans)
