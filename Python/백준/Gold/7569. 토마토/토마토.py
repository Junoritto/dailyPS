from collections import deque

M, N, H = map(int,input().split())
graph = []
for i in range(H):
  temp = []
  for j in range(N):
    arr = list(map(int,input().split()))
    temp.append(arr)
  graph.append(temp)

tomatoes = []

for i in range(H):
  for j in range(N):
    for k in range(M):
      if graph[i][j][k] == 1:
        tomatoes.append([i,j,k,0])


dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs(graph, tomatoes):
  day = 0
  q = deque()
  for tomato in tomatoes:
    q.append(tomato)
  while q:
    cz,cy,cx,day = q.popleft()
    for i in range(6):
      nz = cz + dz[i]
      ny = cy + dy[i]
      nx = cx + dx[i]
      if nz >= 0 and nz < H and ny >= 0 and ny < N and nx >=0 and nx < M:
        if graph[nz][ny][nx] == 0:
          q.append([nz,ny,nx,day+1])
          graph[nz][ny][nx] = 1
  return day

day = bfs(graph, tomatoes)

# 모든 토마토 익었는지 체크
for i in range(H):
  for j in range(N):
    for k in range(M):
      if graph[i][j][k] == 0:
        day = -1


print(day)

  