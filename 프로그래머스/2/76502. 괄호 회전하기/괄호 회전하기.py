from collections import deque

def solution(s):
    arr=deque(list(s))
    answer = 0
    
    check_dict = {")":"(","}":"{","]":"["}
    
    for i in range(len(s)):
        stack = []
        arr.rotate(1)
        
        flag = True
        
        for item in arr:
            if item in [")","}","]"]:
                if (not stack) or stack[-1]!=check_dict[item]:
                    flag = False
                    break
                else:
                    stack.pop()
            else:
                stack.append(item)
        if not stack and flag:
            answer+=1
            
    return answer