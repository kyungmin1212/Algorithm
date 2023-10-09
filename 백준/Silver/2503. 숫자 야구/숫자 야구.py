n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

answer = 0

def check_strike_ball(candidate,check_num):
    strike, ball = 0,0
    for i in range(3):
        for j in range(3):
            if candidate[i] == check_num[j]:
                if i==j:
                    strike+=1
                else:
                    ball+=1
    return strike, ball


for num in range(100,1000):
    str_num = str(num).zfill(3)

    if len(set(str_num))<3 or "0" in set(str_num):
        continue
    
    flag = True
    for check_num, s, b in arr:
        check_num = str(check_num)
        strike,ball = check_strike_ball(str_num,check_num)
        if s!=strike or b!=ball:
            flag=False
            break
    if flag:
        answer+=1
print(answer)