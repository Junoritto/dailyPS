import sys
input = sys.stdin.readline

from collections import Counter

T = int(input())
n = int(input())
nList = list(map(int,input().split()))
m = int(input())
mList = list(map(int,input().split()))

def get_all_sub_sums(lst):
    subs = []
    for i in range(len(lst)):
        total = 0
        for j in range(i, len(lst)):
            total += lst[j]
            subs.append(total)
    return subs

sumA = get_all_sub_sums(nList)
sumB = get_all_sub_sums(mList)

counterA = Counter(sumA)
counterB = Counter(sumB)

answer = 0

for i in counterA:
    answer += counterA[i]*counterB[T-i]

print(answer)
