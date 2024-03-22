from heapq import heappush,heappop
def solution(targets):
    targets.sort()
    answer =0
    
    arive = 0
    for s,e in targets:
        if s>=arive:
            arive = e
            answer+=1
        else:
            arive = min(arive,e)
        
    return answer