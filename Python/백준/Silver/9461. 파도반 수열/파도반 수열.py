dp = [0,1,1,1,2,2]

for i in range(6,101):
    dp.append(dp[i-5]+dp[i-1])

T = int(input())
for i in range(T):
    n = int(input())
    print(dp[n])
