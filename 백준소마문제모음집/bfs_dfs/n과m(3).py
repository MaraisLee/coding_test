# 백트레킹 dfs, 실버3
# https://www.acmicpc.net/problem/15651

n, m = map(int, input().split())
array = []

def dfs():
    if len(array) == m:
        print(' '.join(map(str, array)))
        return
    
    for i in range(1, n + 1):
        array.append(i)
        dfs()
        array.pop()

dfs()
