# dp, 골드5
# https://www.acmicpc.net/problem/2293

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0] * (k+1)
# 1원쓸때 필요함
dp[0] = 1

for c in coins:
    for i in range(c, k + 1):
            # 100원 - 10원(c)일 때의(90원) 동전갯수(dp[90])와 현재 금액횟수를 더하면 됨
            dp[i] += dp[i-c]
        
print(dp[k])