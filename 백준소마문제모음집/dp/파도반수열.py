# dp, 실버3
# https://www.acmicpc.net/problem/9461

n = int(input())
cases = [int(input()) for _ in range(n)]
d = [0] * 101
d[1],d[2], d[3] = 1, 1, 1

for i in range(4, 101):
    d[i] = d[i-3] + d[i-2]
    
    
for case in cases:
    print(d[case])