import heapq
import sys

input = sys.stdin.readline

plus_heap = []
minus_heap = []


N = int(input())
for _ in range(N):
    command = int(input())
    if command == 0:
        if len(minus_heap) == 0 and len(plus_heap) == 0:
            print(0)
        elif len(minus_heap) == 0: # plus heap만 있을 때
            print(heapq.heappop(plus_heap))
        elif len(plus_heap) == 0: # minus heap만 있을 때
            print(heapq.heappop(minus_heap)*-1)
        else:
            plus_temp = heapq.heappop(plus_heap)
            minus_temp = heapq.heappop(minus_heap)
            if minus_temp <= plus_temp:
                print(minus_temp*-1)
                heapq.heappush(plus_heap, plus_temp)
            else:
                print(plus_temp)
                heapq.heappush(minus_heap, minus_temp)
    elif command > 0:
        heapq.heappush(plus_heap, command)
    else:
        heapq.heappush(minus_heap, command*-1)