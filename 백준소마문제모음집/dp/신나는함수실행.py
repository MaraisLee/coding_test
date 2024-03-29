# dp, 실버2
# https://www.acmicpc.net/problem/9184

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    
    # 해당 값이 이미 존재하면 덮어 씌운다. 이 코드가 없다면 기존 재귀와 동일
    if dp[a][b][c]:
        return dp[a][b][c]

    if a < b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[a][b][c] 
    
# 3차원 배열 최악의 경우: 20 * 20 * 20 = 8000번의 계산 
dp = [[[0]* 21 for _ in range(21)] for _ in range(21)]

while 1: 
    a, b, c  = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')