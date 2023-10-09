n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

answer = 0

for num in range(100,1000):
    str_num = str(num).zfill(3)

    if len(set(str_num))<3 or "0" in set(str_num):
        continue
    
    flag = True
    for check_num, s, b in arr:
        check_num = str(check_num)
        if str_num[0]==check_num[0]:
            s-=1
            if s<0:
                flag = False
                break
        elif str_num[0]==check_num[1] or str_num[0]==check_num[2]:
            b-=1
            if b<0:
                flag = False
                break

        if str_num[1]==check_num[1]:
            s-=1
            if s<0:
                flag = False
                break
        elif str_num[1]==check_num[0] or str_num[1]==check_num[2]:
            b-=1
            if b<0:
                flag = False
                break

        if str_num[2]==check_num[2]:
            s-=1
            if s<0:
                flag = False
                break
        elif str_num[2]==check_num[0] or str_num[2]==check_num[1]:
            b-=1
            if b<0:
                flag = False
                break

        if s!=0 or b!=0:
            flag = False
            break
    if flag:
        answer+=1
print(answer)