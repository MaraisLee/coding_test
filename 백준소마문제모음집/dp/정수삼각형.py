# DP, 실버1
# https://www.acmicpc.net/problem/1932


n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]

# 2차원 배열로 봤을 때, 왼쪽 위나 바로 위에서 내려오는 값을 더하면 된다. 
for i in range(1, n):
    for j in range(i + 1):
        # 2차원 배열로 봤을 때, 인덱스가 0번이면 왼쪽 위에는 아무것도 없다
        if j == 0:
            up_left = 0 
        else:
            up_left = d[i-1][j-1]
        # ex) (3,3)인 위치일때, 바로 위쪽에는 아무것도 없다
        if j == i: 
            up = 0
        else:
            up = d[i-1][j]
        # 내 값 + 위에서 받아올 값중 큰 것 
        d[i][j] = d[i][j] + max(up_left,up)
print(max(d[n-1]))

# 어렵다.. 2차원배열을 그냥 외우자, 위아래는 x, 좌우는 y