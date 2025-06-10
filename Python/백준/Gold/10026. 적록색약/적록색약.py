from collections import deque
from copy import deepcopy

N = int(input())
graph = []
for i in range(N):
    line = input()
    graph.append(list(line))

blind_graph = deepcopy(graph)

for i in range(N):
    for j in range(N):
        if blind_graph[i][j] == 'G':
            blind_graph[i][j] = 'R'

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(graph, startR, startC, color):
    q = deque([[startR, startC]])
    graph[startR][startC] = 'X'
    while q:
        cr, cc = q.popleft()
        for i in range(4):
            nr = cr + dx[i]
            nc = cc + dy[i]
            if (nr>=0 and nr<N and nc>=0 and nc<N):
                if graph[nr][nc] == color:
                    q.append([nr,nc])
                    graph[nr][nc] = 'X'
                    

normal_cnt = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] != 'X':
            bfs(graph,i,j,graph[i][j])
            normal_cnt += 1

blind_cnt = 0
for i in range(N):
    for j in range(N):
        if blind_graph[i][j] != 'X':
            bfs(blind_graph,i,j,blind_graph[i][j])
            blind_cnt += 1

print(normal_cnt, blind_cnt)