import sys

input = sys.stdin.readline

n,k = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

dp = [0 for _ in range(k+1)]

for w,v in arr:
    for i in reversed(range(1,k+1)):
        if i>=w:
            dp[i]=max(dp[i],dp[i-w]+v)

print(dp[-1])