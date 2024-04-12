def solution(distance, rocks, n):
    # 최솟값이 크면 n이 커짐
    # 최솟값이 작아지면 n이 작아짐
    # 우리는 n이 딱 맞으면서 최솟값이 커지는걸원함
    # 즉, 단조증가(제일 오른쪽)
    rocks.sort()
    rocks.append(distance)
    start,end = 1, distance+1
    while start<end:
        mid = (start+end)//2
        
        point = 0
        count = 0
        for rock in rocks:
            if rock-point>=mid:
                point=rock
            else:
                count+=1
        if count<=n:
            start = mid+1
        else:
            end = mid
            
    return start-1