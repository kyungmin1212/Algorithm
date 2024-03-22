import sys

sys.setrecursionlimit(int(1e6))

def find(n,m,now_r,now_c,r,c,remain,route):
    global answer
    if len(answer)==1:
        return
    if abs(r-now_r)+abs(c-now_c)>remain:
        return
    
    if remain==0 and now_r==r and now_c==c:
        answer.append(route)
        return
    
    for move in ["d","l","r","u"]:
        if move=="d":
            dr,dc= 1,0
        elif move=="l":
            dr,dc= 0,-1
        elif move=="r":
            dr,dc= 0, 1
        elif move=="u":
            dr,dc = -1,0
        
        next_r,next_c = now_r+dr, now_c+dc
        if next_r<=0 or next_c<=0 or next_r>n or next_c>m:
            continue
        find(n,m,next_r,next_c,r,c,remain-1,route+move)
    

def solution(n, m, x, y, r, c, k):
    global answer
    answer = []

    if (abs(x-r)+abs(y-c))%2!=k%2:
        return "impossible"

    find(n,m,x,y,r,c,k,"")
    if not answer:
        return "impossible" 
    return answer[0]