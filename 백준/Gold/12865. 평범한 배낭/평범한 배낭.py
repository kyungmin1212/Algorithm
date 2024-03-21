import sys

input = sys.stdin.readline

n, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

dp = [0 for _ in range(k + 1)]

for w, v in arr:
    for i in reversed(range(w, k + 1)):
        dp[i] = max(dp[i], dp[i - w] + v)

print(max(dp))
