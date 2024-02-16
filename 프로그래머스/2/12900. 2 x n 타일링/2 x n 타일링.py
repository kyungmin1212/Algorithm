def solution(n):
    answer = 0
    dp = [0 for _ in range(n+1)]
    if n==1:
        return 1
    elif n==2:
        return 2
    
    dp[1]=1
    dp[2]=2
    
    for i in range(3,n+1):
        dp[i]=((dp[i-2]%1000000007)+(dp[i-1]%1000000007))%1000000007
        
    return dp[n]