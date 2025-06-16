from collections import deque
import sys

input = sys.stdin.readline

T = int(input())
for i in range(T):
    visited = [False] * 10000
    A, B = map(int,input().split())
    q = deque([[A,'']])
    visited[A] = True
    while q:
        v, his = q.popleft()
        if v == B:
            print(his)
            break
        # D
        dv = v*2
        if dv > 9999:
            dv = dv % 10000
        if visited[dv] == False:
            dhis = his + 'D'
            q.append([dv, dhis])
            visited[dv] = True
        # S
        sv = v-1
        if sv == -1:
            sv = 9999
        if visited[sv] == False:
            shis = his + 'S'
            q.append([sv, shis])
            visited[sv] = True
        # L
        cheon = v // 1000
        lv = v - (cheon*1000)
        lv *= 10
        lv += cheon
        if visited[lv] == False:
            lhis = his + 'L'
            q.append([lv, lhis])
            visited[lv] = True
        # R
        il = v % 10
        rv = v - il
        if (rv != 0):
            rv //= 10
        rv += (il*1000)
        if visited[rv] == False:
            rhis = his + 'R'
            q.append([rv, rhis])
            visited[rv] = True