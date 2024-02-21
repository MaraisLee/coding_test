# 다이나믹 프로그래밍, 실버3
# https://www.acmicpc.net/problem/1463

n = int(input())
# DP 테이블 초기화
d = [0] * (n + 1)

# DP 보텀업
# 1을 만들어야하기에 2부터 시작
for i in range(2, n + 1):
    # 1. 앞의 숫자의 최소값만드는 방법 횟수  + 1하는 방법 
    d[i] = d[i - 1] + 1  
     # 2. * 2하는 방법
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1 )
     # 3. * 3하는 방법   
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1 )
        
print(d[n])

