import math

def solution(n, k):
    answer = []
    remain_k = k-1
    check_num = [i for i in range(1,n+1)]
    while len(answer)!=n:
        idx = remain_k//math.factorial(n-len(answer)-1)
        remain_k = remain_k%math.factorial(n-len(answer)-1)
        answer.append(check_num[idx])
        del check_num[idx]
        
    return answer