# p.339, 실버2
# [백준] https://www.acmicpc.net/problem/18352

from collections import deque

n, m , k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [-1] * (n + 1)
visited = [False] * (n+1)

for _ in range(m):
    a, b =  map(int, input().split())
    graph[a].append(b) # graph [[], [2, 3], [3, 4], [], []], 1번도시에는 2,3번 도시가 연결되어있다는 의미

def bfs(start):
    answer = []
    q = deque([x])
    visited[start] = True
    # x에서 출발
    distance[start] = 0
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                distance[i] = distance[now] + 1
                q.append(i)
                if distance[i] == k:
                    answer.append(i)
                    
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i)

bfs(x)
    