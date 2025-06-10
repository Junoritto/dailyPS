from collections import defaultdict, deque

dic = defaultdict(int)

N, M = map(int,input().split())
for i in range(N):
    x,y = map(int,input().split())
    dic[x] = y

for i in range(M):
    u,v = map(int,input().split())
    dic[u] = v


visited = [False] * 101

q = deque([[1,0]])
visited[1] = True
while q:
    v,t = q.popleft()
    if v == 100:
        print(t)
        break
    for i in range(1,7):
        nv = v+i
        if nv <= 100:
            if visited[nv] == False:
                if dic[nv] != 0:
                    q.append([dic[nv],t+1])
                else:
                    q.append([nv,t+1])
                visited[nv] = True
            

