import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

tetrominos = [
    # 일자 블록
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    # 2x2 블록
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    # T 블록
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 1), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (1, 1)],
    [(0, 1), (1, 1), (2, 1), (1, 0)],
    # S 블록
    [(1, 0), (0, 1), (1, 1), (0, 2)], 
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(0, 1), (1, 1), (1, 0), (2, 0)],
    # L 블록
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (1, 1), (1, 0)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 1), (1, 1), (2, 1), (2, 0)]
]

max_sum = 0
for i in range(N):
    for j in range(M):
        for t in tetrominos:
            cur = 0
            valid = True

            for dy, dx in t:
                ny, nx = i+dy, j+dx
                if 0 <= ny < N and 0 <= nx < M:
                    cur += board[ny][nx]
                else:
                    valid = False
                    break
            
            if valid == True:
                max_sum = max(max_sum, cur)
print(max_sum)