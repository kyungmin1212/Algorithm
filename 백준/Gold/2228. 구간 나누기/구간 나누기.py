import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [0] + [int(input()) for _ in range(n)]

dp = [[[-float("inf"), -float("inf")] for _ in range(n + 1)] for _ in range(m + 1)]
dp[0] = [[0, 0] for _ in range(n + 1)]

for row in range(1, m + 1):
    for column in range(1, n + 1):
        dp[row][column][0] = max(
            dp[row - 1][column - 1][1] + arr[column],
            dp[row][column - 1][0] + arr[column],
        )
        dp[row][column][1] = max(dp[row][column - 1][0], dp[row][column - 1][1])

print(max(dp[-1][-1]))

# for row in range(1, m + 1):
#     for column in range(1, n + 1):


# print(max(dp[m]))
