import sys
from collections import defaultdict

sys.setrecursionlimit(int(1e6))

input = sys.stdin.readline

n, m = map(int, input().split())

graph = defaultdict(set)
reversed_graph = defaultdict(set)

for i in range(1, n + 1):
    graph[i] = set()
    graph[-i] = set()
    reversed_graph[i] = set()
    reversed_graph[-i] = set()

for _ in range(m):
    a, b = map(int, input().split())
    graph[-a].add(b)
    reversed_graph[b].add(-a)
    graph[-b].add(a)
    reversed_graph[a].add(-b)

def dfs(node):
    visited[node] = True
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)
    check_list.append(node)

def reversed_dfs(node, scc_num):
    visited[node] = True
    sccId[node] = scc_num
    for next_node in reversed_graph[node]:
        if not visited[next_node]:
            reversed_dfs(next_node, scc_num)


visited = defaultdict(lambda :False)
check_list = []

for i in graph.keys():
    if not visited[i]:
        dfs(i)

visited = defaultdict(lambda: False)
sccId = defaultdict(int)
scc_num = 0

for i in reversed(check_list):
    if not visited[i]:
        scc_num += 1
        reversed_dfs(i, scc_num)

flag = True
answer = [-1 for _ in range(n + 1)]
for i in range(1, n + 1):
    if sccId[i] == sccId[-i]:
        flag = False
        break
    answer[i] = int(sccId[i] > sccId[-i])

if flag:
    print(1)
    print(*answer[1:])
else:
    print(0)
