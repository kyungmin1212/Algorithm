import sys
from collections import defaultdict

sys.setrecursionlimit(int(1e6))

input = sys.stdin.readline

n,m= map(int,input().split())

graph = defaultdict(set)
reversed_graph = defaultdict(set)

for _ in range(m):
    a,b = map(int,input().split())
    graph[-a].add(b)
    reversed_graph[b].add(-a)
    graph[-b].add(a)
    reversed_graph[a].add(-b)

def dfs(node):
    visited[node]=True
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)
    check_list.append(node)

def reversed_dfs(node):
    global flag
    if -node in sub_scc:
        flag = False
    sub_scc.add(node)
    visited[node]=True
    for next_node in reversed_graph[node]:
        if not visited[next_node]:
            reversed_dfs(next_node)
    
visited = defaultdict(lambda :False)
check_list = []

for i in list(graph.keys()):
    if not visited[i]:
        dfs(i)

visited = defaultdict(lambda :False)
scc = []

flag = True
for i in reversed(check_list):
    if not visited[i]:
        sub_scc=set()
        reversed_dfs(i)
        if not flag:
            break
if flag:
    print(1)
else:
    print(0)

