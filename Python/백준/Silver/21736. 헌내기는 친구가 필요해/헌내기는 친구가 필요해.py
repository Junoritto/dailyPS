from collections import deque

N,M = map(int,input().split())
graph = []
for i in range(N):
    arr = input()
    lst = []
    for j in range(len(arr)):
        if arr[j] == 'I':
            startX = i
            startY = j
        lst.append(arr[j])
    graph.append(lst)

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(graph, startX, startY):
    answer = 0
    q = deque([[startX,startY]])
    while q:
        x,y = q.popleft()
        for i in range(4):
            cx = x+dx[i]
            cy = y+dy[i]
            if (cx>=0 and cx<N and cy>=0 and cy<M):
                if (graph[cx][cy] == 'O'):
                    q.append([cx,cy])
                    graph[cx][cy] = 'X'
                elif (graph[cx][cy] == 'P'):
                    q.append([cx,cy])
                    graph[cx][cy] = 'X'
                    answer += 1
    if answer == 0:
        return 'TT'
    else:
        return answer


print(bfs(graph, startX, startY))
        