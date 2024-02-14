def solution(plans):
    
    # 과제 시작 시간 시작
    # 새로운 과제 시작시간 -> 기존진행중이던 과제 멈추고 새로운 과제 시작
    # 진행중이던 과제 끝나면 잠시 멈춘과제 다시 이어서 시작
        # 만약 과제 끝낸 시간 에 새로 시작해야되는 과제 잠시 멈춰둔 과제 모두 존재 -> 새로 시작해야하는 과제부터 진행
    # 멈춰둔 과제가 여러개 일경우 가장 최근에 멈춘 과제부터 시작
    # 과제를 끝낸 순서대로 이름을 배열에 담아 RETURN
    
    new_plans =[]
    for name,start,playtime in plans:
        h,m = start.split(":")
        new_plans.append([name,int(h)*60+int(m),int(playtime)])
    new_plans = sorted(new_plans,key=lambda x:x[1])

    len_plans = len(new_plans)
    
    answer = []
    
    remain_stack = []
    for i in range(len_plans-1):
        diff_time = new_plans[i+1][1]-new_plans[i][1]
        if diff_time>=new_plans[i][2]:
            answer.append(new_plans[i][0])
            remain_time = diff_time-new_plans[i][2]
            
            while remain_time>0 and remain_stack:
                name,t = remain_stack.pop()
                if t<=remain_time:
                    remain_time-=t
                    answer.append(name)
                else:
                    t-=remain_time
                    remain_stack.append([name,t])
                    break
        else:
            r_t = new_plans[i][2]-diff_time
            remain_stack.append([new_plans[i][0],r_t])
    
    answer.append(new_plans[-1][0])
    for name,_ in reversed(remain_stack):
        answer.append(name)
        
    
    return answer