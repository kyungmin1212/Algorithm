import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))

parent = [i for i in range(n+1)]
group_sum = arr[:]
group_count = [1] * (n+1)

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a != b:
        if a < b:
            parent[b] = a
            group_sum[a] += group_sum[b]
            group_count[a] += group_count[b]
        else:
            parent[a] = b
            group_sum[b] += group_sum[a]
            group_count[b] += group_count[a]

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

groups = [(group_sum[i], group_count[i]) for i in range(1, n+1) if parent[i] == i and group_count[i] < k]

dp = [0] * k

for candy_count, child_count in groups:
    for j in reversed(range(child_count, k)):
        dp[j] = max(dp[j], dp[j-child_count] + candy_count)

print(max(dp))
