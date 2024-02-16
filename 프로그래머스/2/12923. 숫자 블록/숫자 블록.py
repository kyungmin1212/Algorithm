import math

def find(number):
    if number==1:
        return 0
    sub_answer = []
    for i in range(2,int(math.sqrt(number))+1):
        if number%i==0:
            if (number//i)<=10000000:
                return number//i
            else:
                sub_answer.append(i)
    if sub_answer:
        return max(sub_answer)
    return 1
        

def solution(begin, end):
    answer = []
    for num in range(begin,end+1):
        answer.append(find(num))
    return answer