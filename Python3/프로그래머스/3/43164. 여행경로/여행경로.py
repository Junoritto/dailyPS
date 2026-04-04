from collections import deque

def solution(tickets):
    answer = []
    tickets.sort()
    visited = [False] * len(tickets)
    def dfs(cur, path, visited):
        if len(path) == len(tickets)+1:
            return path
        for i in range(len(tickets)):
            if not visited[i] and tickets[i][0] == cur:
                visited[i] = True
                result = dfs(tickets[i][1], path + [tickets[i][1]], visited)
                if result:
                    return result
                visited[i] = False
    return dfs("ICN", ["ICN"], visited)
        