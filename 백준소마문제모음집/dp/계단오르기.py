# DP, 백준 실버3
# [https://www.acmicpc.net/problem/2579]

n = int(input())
# 계단 리스트 받기
stairs = [int(input()) for _ in range(n)]
d = [0] * (n)

# 2개 이하일 경우에는 무조건 다 밟아야하므로 sum 
if len(stairs) <= 2:
    print(sum(stairs))
else:
    # 1,2번째는 수동 (무조건이므로)
    d[0] = stairs[0]
    d[1] = stairs[0] + stairs[1]
    
    for i in range(2, n):
        # 마지막 도착 계단은 반드시 밟아야 한다.는 조건이 있으므로 마지막계단에서 점화식을 생각 
        d[i] = max((d[i-3] + stairs[i-1] + stairs[i]), (d[i-2] + stairs[i] ))
    
    # 계단인데스와 맞추기 위해서 n + 1이 아닌 n으로 진행하고 마지막에 인덱스에서 -1    
    print(d[-1])
