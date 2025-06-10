import heapq
import sys

input = sys.stdin.readline

T = int(input())
for i in range(T):
    k = int(input())
    min_heap = []
    max_heap = []
    visited = [False] * k
    for j in range(k):
        command, n = input().split()
        n = int(n)
        if command == 'I':
            heapq.heappush(min_heap, (n,j))
            heapq.heappush(max_heap, (-n,j))
            visited[j] = True
        elif command == 'D':
            if n == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            elif n == -1:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
    
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    
    if not min_heap:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])
