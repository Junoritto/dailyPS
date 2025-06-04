from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]
answer_graph = [[0] * N for _ in range(N)]

for i in range(N):
    arr = list(map(int,input().split()))
    for j in range(N):
        if arr[j] == 1:
            graph[i+1].append(j+1)

def bfs(graph, start, visited):
    q = deque([start])
    while q:
        v = q.popleft()
        if visited[v] == True:
            answer_graph[start-1][v-1] = 1
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


for i in range(1,N+1):
    visited = [False] * (N+1)
    bfs(graph, i, visited)

for i in range(N):
    for j in range(N):
        print(answer_graph[i][j], end=' ')
    print()