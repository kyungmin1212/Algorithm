def solution(distance, rocks, n):
    answer = 0
    rocks = sorted(rocks)
    
    start = 1
    end = distance
    
    while start<=end:
        mid = (start+end)//2
        
        rock_count = 0
        now_point = mid
        for rock in rocks:
            if now_point<=rock:
                now_point = rock+mid
                rock_count+=1
            else:
                continue
        if now_point>distance: # 제일 끝에 돌을 제거해야함.
            rock_count-=1
                
        if rock_count>=len(rocks)-n:
            start=mid+1
            answer=mid
        else:
            end=mid-1
    
    return answer