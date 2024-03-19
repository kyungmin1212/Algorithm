def solution(heights):
    heights.sort()
    
    n_heights = len(heights)
    if n_heights%2==0: # 짝수개 인경우
        new_arr=[]
        for i in range(n_heights//2):
            new_arr.append(heights[n_heights//2+i])
            new_arr.append(heights[i])
        
        diff = []
        for i in range(n_heights-1):
            diff.append(abs(new_arr[i+1]-new_arr[i]))
        diff.sort()
        return diff[0]
    else:
        new_arr=[]
        for i in range(n_heights//2):
            new_arr.append(heights[i])
            new_arr.append(heights[n_heights//2+1+i])
        new_arr.append(heights[n_heights//2])
        new_arr.append(heights[0]) # 제일 작은 값을 찾기 위함.
        
        diff = []
        for i in range(len(new_arr)-1):
            diff.append(abs(new_arr[i+1]-new_arr[i]))
        diff.sort()
        return diff[1] 
