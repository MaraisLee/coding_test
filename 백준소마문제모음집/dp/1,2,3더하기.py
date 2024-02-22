# DP, 백준 실버3
# https://www.acmicpc.net/problem/9095

n = int(input())
n_list = [int(input()) for _ in range(n)]
d = [0] * 11
d[1] = 1
d[2] = 2
d[3] = 4
d[4] = 7

# 1,2,3으로만 더할 수 있음
for i in range(5, 11):
    d[i] = d[i-3] + d[i-2] + d[i-1]

for j in n_list:
    print(d[j])