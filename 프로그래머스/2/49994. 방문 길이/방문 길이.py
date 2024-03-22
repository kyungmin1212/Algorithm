from collections import defaultdict

def solution(dirs):
    orderdict = {"U":(0,1),"D":(0,-1),"R":(1,0),"L":(-1,0)}
    visited = defaultdict(int)
    
    answer = 0
    now_x,now_y = 0,0
    for order in dirs:
        dx,dy = orderdict[order]
        next_x,next_y = now_x+dx, now_y+dy
        if next_x<-5 or next_x>5 or next_y<-5 or next_y>5:
            continue
        if visited[(now_x,now_y,next_x,next_y)] or visited[(next_x,next_y,now_x,now_y)]:
            pass
        else:
            visited[(now_x,now_y,next_x,next_y)]=1
            answer+=1
        
        now_x, now_y = next_x,next_y
    return answer