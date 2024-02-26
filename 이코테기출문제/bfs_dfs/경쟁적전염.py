# p.344
# https://www.acmicpc.net/problem/18405

from collections import deque

n, k = map(int, input().split()) 
graph = [list(map(int, input().split())) for _ in range(n)]
data = []
s, x, y = map(int, input().split()) 
directions = [(0,1),(0,-1),(1,0),(-1,0)]

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            # 각 위치의 바이러스 종류, 시간, 위치 정보 넣기
            data.append((graph[i][j], 0, i, j))

def bfs():
    q = deque(data)
    while q:
        virus, time, x, y = q.popleft()
        # target time이 되면 빠져나가기
        if time == s:
            break
        for dx, dy in directions:
            nx, ny = dx + x, dy + y
            # if not (0 <= nx < n  and 0 <= ny < n):
            #     continue
            # if  graph[nx][ny] != 0:
            #     continue
            if 0 <= nx < n  and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, time+1, nx, ny))
    return graph[x-1][y-1]

# 번호가 낮은 종류부터 증식
data.sort()
bfs()
print(graph[x-1][y-1])