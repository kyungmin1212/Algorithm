from bisect import bisect_right

def solution(numbers):
    answer = []
    check_list = []
    
    for num in reversed(numbers):
        idx = bisect_right(check_list,num)
        check_list = check_list[idx:]
        if not check_list:
            answer.append(-1)
        else:
            answer.append(check_list[0])
        check_list= [num]+check_list
    
    return answer[::-1]