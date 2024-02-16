import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
parent = [i for i in range(n + 1)]


def find(x):
    if x == parent[x]:
        return x

    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return False
    elif a > b:
        parent[b] = a
    else:
        parent[a] = b

    return True


answer = 0
graph = []
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append([a, b, c])

graph.sort(key=lambda x: x[2])

for a, b, c in graph:
    if union(a, b):
        answer += c

print(answer)
