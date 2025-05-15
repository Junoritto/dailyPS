import sys
input = sys.stdin.readline

dp = [[[[] for _ in range(21)] for _ in range(21)] for _ in range(21)]


for x in range(21):
    for y in range(21):
        for z in range(21):
            if x == 0 or y == 0 or z == 0:
                dp[x][y][z] = 1
                continue
            if x<y and y<z:
                dp[x][y][z] = dp[x][y][z-1] + dp[x][y-1][z-1] - dp[x][y-1][z]
            else:
                dp[x][y][z] = dp[x-1][y][z] + dp[x-1][y-1][z] + dp[x-1][y][z-1] - dp[x-1][y-1][z-1]

while True:
    a,b,c = map(int,input().split())
    ans = 0
    if a == -1 and b == -1 and c == -1:
        break
    if a <= 0 or b <= 0 or c <= 0:
        ans = 1
    elif a > 20 or b > 20 or c > 20:
        ans = dp[20][20][20]
    else:
        ans = dp[a][b][c]
    print(f'w({a}, {b}, {c}) = {ans}')
