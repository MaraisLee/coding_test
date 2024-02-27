# dp, 실버1
# https://www.acmicpc.net/problem/11052

n = int(input())
data = list(map(int, input().split()))
data.insert(0,0)
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, i+1):
        # ex) dp[4] = (dp[3] + data[1], dp[2] + data[2], dp[1] + data[3), data[4]
        dp[i] = max(dp[i], dp[i-j] + data[j])
print(dp[n])