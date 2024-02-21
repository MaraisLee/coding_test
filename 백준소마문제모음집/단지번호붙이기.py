# dfs, bfs?, 실버1
# https://www.acmicpc.net/problem/2667

from collections import deque

n = int(input())
graph = [list(map(int,input())) for _ in range(n)]
visited = [[False]* n for _ in range(n)]
answer = []
# 방향 설정
direction = [(0, 1), (0, -1), (1, 0), (-1,0)]

def bfs(x, y):
    visited[x][y] = True
    q = deque()
    # [x, y] 형태는 바로 depue([x,y])에 못 집어 넣는다. 따라서 append 사용!
    q.append([x, y])
    cnt = 1
    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            # 현재 위치에서 상하좌우 확인
            nx, ny = x + dx, y + dy
            if 0<= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    cnt += 1
                    visited[nx][ny] = True
                    q.append([nx, ny])
    return cnt

for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            answer.append(bfs(i, j))

print(len(answer))
answer.sort()
for i in answer:
    print(i)

