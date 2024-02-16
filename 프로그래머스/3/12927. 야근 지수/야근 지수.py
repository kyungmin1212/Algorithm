from heapq import heappush,heappop

def solution(n, works):
    answer = 0
    if n>=sum(works):
        return 0
    
    q = []
    for work in works:
        heappush(q,-work)

    remain_n = n
    while remain_n>0:
        first_v = -heappop(q)
        if len(q)>=1:
            if first_v>=-q[0]:
                first_v-=1
                remain_n-=1
        heappush(q,-first_v)
    
    
    return sum([item**2 for item in q])