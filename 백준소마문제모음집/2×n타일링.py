# DP, 실버3
# https://www.acmicpc.net/problem/11726

n = int(input())
d = [0] * 1001 # 런타임에러가 발생할 수 있으므로 n + 1 보다 숫자 제한두기 
d[1], d[2], d[3] = 1, 2, 3

for i in range(4, n + 1 ):
    # 주욱 나열하다 보면 점화식 아래처럼 나옴 (종이에 나열해보기)
    d[i] = (d[i-2] + d[i-1]) %10007
    
print(d[n])