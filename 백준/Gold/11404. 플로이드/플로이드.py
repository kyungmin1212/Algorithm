import sys

input = sys.stdin.readline

n = int(input())

m = int(input())

distance = [[float("inf") for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    distance[s][e] = min(distance[s][e], w)

for i in range(1, n + 1):
    distance[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if distance[i][j] == float("inf"):
            print(0, end=" ")
        else:
            print(distance[i][j], end=" ")
    print()
