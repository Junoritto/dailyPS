import sys
input = sys.stdin.readline

import heapq

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
degree = [-1] + ([0] * (N))
ansList = []

for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    degree[b] += 1

pq = []
for i in range(1, N+1):
    if degree[i] == 0:
        heapq.heappush(pq, i)

while pq:
    current = heapq.heappop(pq)
    result = ansList.append(current)

    for node in graph[current]:
        degree[node] -= 1
        if degree[node] == 0:
            heapq.heappush(pq, node)

for answer in ansList:
    print(answer, end=' ')