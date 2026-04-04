from collections import deque

def solution(begin, target, words):
    answer = 0
    visited = [False] * len(words)
    def bfs(begin, target, visited):
        q = deque([(begin,0)])
        while q:
            cur, depth = q.popleft()
            if cur == target:
                return depth
            for i in range(len(words)):
                if not visited[i]:
                    length = len(cur)
                    diff = 0
                    for j in range(length):
                        if cur[j] != words[i][j]:
                            diff += 1
                    if diff == 1:
                        q.append((words[i], depth+1))
                        visited[i] = True
    
    return bfs(begin, target, visited) or 0