# DP, 실버1
# https://www.acmicpc.net/problem/1149

n = int(input())
d = [0] * n 
for i in range(n):
    d[i] = list(map(int,input().split()))
    
for i in range(1, n):
    # 여기서 첫번째집 최소값을 더해주기때문에 1부터 시작 
    d[i][0] = min(d[i-1][1],d[i-1][2]) + d[i][0]
    d[i][1] = min(d[i-1][0],d[i-1][2]) + d[i][1]
    d[i][2] = min(d[i-1][0],d[i-1][1]) + d[i][2]

# 순차적으로 최솟값만 더해져 있는 상태이기 때문에 마지막에는 본인의 빨, 초, 파 비용중 최솟값을 고르면된다. 
print(min(d[n-1]))


