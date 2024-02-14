def solution(m, n, startX, startY, balls):
    answer = []
    # 꼭지점은 그냥 진입방향의 반대방향으로 공이 진행됨.
    for ball_x,ball_y in balls:

        if startY==ball_y and ball_x>startX:
            ans1=int(1e9)
        else:
            ans1 = (startX-(ball_x+(m-ball_x)*2))**2+(startY-ball_y)**2
        
        if startX==ball_x and ball_y>startY:
            ans2=int(1e9)
        else:
            ans2 = (startX-ball_x)**2+(startY-(ball_y+(n-ball_y)*2))**2
            
        if startY==ball_y and ball_x<startX:
            ans3=int(1e9)
        else:
            ans3 = (startX+ball_x)**2+(startY-ball_y)**2
        
        if startX==ball_x and ball_y<startY:
            ans4=int(1e9)
        else:
            ans4 = (startX-ball_x)**2+(startY+ball_y)**2
        
        min_ans = min(ans1,ans2,ans3,ans4)
        
        answer.append(min_ans)
    return answer