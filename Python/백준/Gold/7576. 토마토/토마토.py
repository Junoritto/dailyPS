import sys
input = sys.stdin.readline

from collections import deque

m,n = map(int,input().split())
graph = []
start = deque()
for i in range(n):
    arr = list(map(int,input().split()))
    graph.append(arr)
    for j in range(m):
        if graph[i][j] == 1:
            start.append([i,j,0])

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(graph, start):
    day = 0
    q = start
    while q:
        r,c,day = q.popleft()
        for i in range(4):
            cr = r+dx[i]
            cc = c+dy[i]
            if cr>=0 and cr<n and cc>=0 and cc<m:
                if graph[cr][cc] == 0:
                    q.append([cr,cc,day+1])
                    graph[cr][cc] = 1
    return day

day = bfs(graph, start)
for i in range(n):
    if 0 in graph[i]:
        day = -1

print(day)


