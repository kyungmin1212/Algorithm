def solution(s):
    answer = []
    # 문자를 stack 에 쌓으면서 마지막 3개가 110인지 파악
    # 그리고 나서 모든 110 들을 제거해주고 110은 무조건 111보다 앞에있을경우에만 사전순이 빠름.
    # 따라서 110 이 다른값보다 앞에있으면 뒤로 보내줘야하고 111보다 뒤에 있으면 앞으로 보내줘야함.
    # 즉, stack을 뒤에서부터 체크하다가 0이 보이면 더이상 가면 안되고 그 위치에 110을 넣어주어함.
    
    for string in s:
        stack = []
        count_110 = 0
        for i in range(len(string)):
            stack.append(string[i])
            if len(stack)>=3 and stack[-3:]==['1','1','0']:
                for _ in range(3):
                    stack.pop()
                count_110+=1
        zero_flag = False
        for i in reversed(range(len(stack))):
            if stack[i]=='0':
                zero_flag = True
                break
        if zero_flag:
            ans = stack[:i+1]+['1','1','0']*count_110+stack[i+1:]
        else:
            ans = ['1','1','0']*count_110+stack
        answer.append("".join(ans))
    return answer