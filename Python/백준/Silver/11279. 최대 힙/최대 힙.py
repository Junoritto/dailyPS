import heapq
import sys

input = sys.stdin.readline

heap = []

N = int(input())
for i in range(N):
    command = int(input())
    if command == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap) * -1)
    else:
        heapq.heappush(heap, command * -1)
