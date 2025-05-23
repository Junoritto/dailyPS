db = {}
N, M = map(int,input().split())
for i in range(N):
    site, pw = input().split()
    db[site] = pw
for i in range(M):
    target = input()
    print(db[target])