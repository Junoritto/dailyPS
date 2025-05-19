import sys
input = sys.stdin.readline

from collections import deque

stage = []
answer_stage = []

n, m = map(int,input().split())
for i in range(n):
    arr = list(map(int,input().split()))
    for j in range(len(arr)):
        if arr[j] == 2:
            startR = i
            startC = j
    stage.append(arr)

answer_stage = [[0] * m for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]


def bfs(stage, startR, startC, answer_stage):
    q = deque([[startR,startC]])
    while q:
        r,c = q.popleft()
        for i in range(4):
            cr = r+dx[i]
            cc = c+dy[i]
            if cr>=0 and cr<n and cc>=0 and cc<m:
                if stage[cr][cc] == 1:
                    q.append([cr,cc])
                    answer_stage[cr][cc] = answer_stage[r][c] + 1
                    stage[cr][cc] = -1

bfs(stage, startR, startC, answer_stage)

for i in range(n):
    for j in range(m):
        if stage[i][j] == 1:
            answer_stage[i][j] = -1

for i in range(n):
    for e in answer_stage[i]:
        print(e, end=' ')
    print()

