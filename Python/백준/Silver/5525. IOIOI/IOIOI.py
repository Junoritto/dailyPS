import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().strip()

cursor, cnt, res = 0, 0, 0

while cursor < (M-1):
    if S[cursor:cursor+3] == 'IOI':
        cnt += 1
        cursor += 2
        if cnt == N:
            res += 1
            cnt -= 1
    else:
        cursor += 1
        cnt = 0
print(res)

