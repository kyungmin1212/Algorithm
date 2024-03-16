def solution(distance, rocks, n):
    rocks = sorted(rocks)+[distance]
    
    start,end = 1,distance+1
    
    while start<end:
        mid = (start+end)//2
        
        output = 0
        before_point = 0
        
        for d in rocks:
            if d-before_point>=mid:
                before_point=d
            else:
                output+=1
        
        if output<=n:
            start = mid+1
        else:
            end = mid
            
    return start-1
