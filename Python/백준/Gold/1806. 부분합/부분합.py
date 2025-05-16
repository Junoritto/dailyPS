import sys
input = sys.stdin.readline

N, S = map(int,input().split())
arr = list(map(int,input().split()))

left = 0
right = 1
cur = arr[0]
ans = N

if sum(arr) < S:
    print(0)
else:
    while True:
        if cur<S:
            if right == N:
                break
            cur += arr[right]
            right += 1
        else:
            ans = min(right-left, ans)
            cur -= arr[left]
            left += 1

    print(ans)

