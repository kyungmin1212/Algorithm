import math

def find(binary_str,left,right,zero_flag): # zero_flag = True면 그다음 과정에서 1이 있으면 안됩니다.
    if left==right:
        if zero_flag and binary_str[left]=="1":
            return False
        else: # zero_flag가 0이지만 자식 노드도 0이면 가능한경우
            return True
    
    mid = (left+right)//2
    if zero_flag:
        if binary_str[mid]=="1": # zero_flag가 0이면서 중간에 1을 만나면 False리턴
            return False
        else: # 0 인경우 계속 탐색 해야함
            flag1 = find(binary_str,left,mid-1,zero_flag)
            flag2 = find(binary_str,mid+1,right,zero_flag)
            return flag1&flag2
    else:
        if binary_str[mid]=="1":
            flag1 = find(binary_str,left,mid-1,False)
            flag2 = find(binary_str,mid+1,right,False)
            return flag1&flag2
        else: # 0이면 다음 단계에서 
            flag1 = find(binary_str,left,mid-1,True)
            flag2 = find(binary_str,mid+1,right,True)
            return flag1&flag2       

    

def solution(numbers):
    answer = []
    for num in numbers:
        num_len = len(bin(num))-2
        square =  math.floor(math.log2(num_len))
        total_len = 2**(square+1)-1
        
        total_bin = "0"*(total_len-num_len)+bin(num)[2:]
        answer.append(int(find(total_bin,0,total_len-1,False)))
    return answer