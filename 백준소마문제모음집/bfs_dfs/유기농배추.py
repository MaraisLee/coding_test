# dfs, 실버2
# https://www.acmicpc.net/problem/1012

# recursion error 뜨면 아래코드 추가
import sys
sys.setrecursionlimit(10**7)

def dfs(x, y):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        # nx :  세로, ny : 가로 범위 내
        if (0 <= nx < n) and (0 <= ny < m):
            # 즉, 0 이면 다시 for 문 -> directions 다 돌면 -> dfs 종료
            # 1이 있는 공간은 다 돌다가 빠져나옴
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                dfs(nx, ny)

# case 횟수
t = int(input())
# 가로, 세로, 1의 개수(배추있는곳)
# 아래는 케이스 횟수만큼 반복되는 코드
for case in range(t):
    m, n, k = map(int, input().split())
    # 0 * m 하면 1차원배열, [0] * m 하면 2차원배열 생성
    graph = [[0] * m for _ in range(n)]
    count = 0
    # 케이스 받아서 graph에 적용 (2차원배열그리기)
    for i in range(k):
        M, N = map(int, input().split())
        # 배열은 기존의 좌표 평면 x, y축과 반대다 (x: 좌우, y: 상하)
        graph[N][M] = 1
        
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 1:
                dfs(x, y)
                count += 1
        
    print(count)

