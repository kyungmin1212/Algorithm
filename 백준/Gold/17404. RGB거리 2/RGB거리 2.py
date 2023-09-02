n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

dp = [float('inf') for _ in range(3)]

answer_list = []
for (s,e) in ((0,1),(0,2),(1,0),(1,2),(2,0),(2,1)):
    dp[s]=arr[0][s]
    for i in range(1,n-1):
        dp = [min(dp[1],dp[2])+arr[i][0],min(dp[0],dp[2])+arr[i][1],min(dp[0],dp[1])+arr[i][2]]
    if e==0:
        answer_list.append(min(dp[1],dp[2])+arr[-1][0])
    elif e==1:
        answer_list.append(min(dp[0],dp[2])+arr[-1][1])
    elif e==2:
        answer_list.append(min(dp[0],dp[1])+arr[-1][2])

print(min(answer_list))