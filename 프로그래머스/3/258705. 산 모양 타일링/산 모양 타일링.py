def solution(n, tops):
    
    dp = [0 for _ in range(n*2+1)]
    if tops[0]==1:
        dp[1]=2
    else:
        dp[1]=1
    for i in range(2,n*2+1):
        if i%2==1:
            if tops[i//2]==1:
                dp[i]=dp[i-1]+dp[i-2]+1+dp[i-1]+1
            else:
                dp[i]=dp[i-1]+dp[i-2]+1
        else:
            dp[i]=dp[i-1]+dp[i-2]+1
        dp[i]=dp[i]%10007
                
    return (dp[-1]+1)%10007