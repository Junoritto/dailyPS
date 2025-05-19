import sys
input = sys.stdin.readline


N, M = map(int,input().split())
trees = list(map(int,input().split()))

def cut(trees, length):
    result = 0
    for i in range(N):
        cut_tree = max(0,trees[i]-length)
        result += cut_tree
    return result

start = 0
end = max(trees)
flag = 0
while (start < end):
    mid = (start+end) // 2 + 1
    cut_length = cut(trees,mid)
    if cut_length > M:
        start = mid
    elif cut_length == M:
        answer = mid
        flag = 1
        break
    else:
        end = mid-1

if flag == 0:
    print(end)
else:
    print(answer)