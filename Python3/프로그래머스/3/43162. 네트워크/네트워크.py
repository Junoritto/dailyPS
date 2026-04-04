from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * (n)
    def bfs(start,computers,visited):
        q = deque([start])
        visited[start] = True
        while q:
            n = q.popleft()
            for i in range(len(computers[n])):
                if n != i and computers[n][i] == 1 and not visited[i]:
                    q.append(i)
                    visited[i] = True

    for i in range(n):
        if not visited[i]:
            bfs(i,computers,visited)
            answer += 1
    return answer