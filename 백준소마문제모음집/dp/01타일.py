# dp, 실버3
# https://www.acmicpc.net/problem/1904

n = int(input())
# [0] * (n + 1)하면 indexError 난다. 한게를 정해주자
d = [0] * 1000001
d[1], d[2] = 1, 2

for i in range(3, n+1):
    # 하드코딩해보면 아래같은 규칙 보임
    d[i] = (d[i - 1] + d[i - 2] ) % 15746

print(d[n])