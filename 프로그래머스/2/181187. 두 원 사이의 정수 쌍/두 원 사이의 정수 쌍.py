import math

def solution(r1, r2):
    count = 0
    for i in range(1,r2+1):
        if i>=r1:
            y_min = 0
        else:
            y_min = math.sqrt(r1**2-i**2)

        y_max = math.sqrt(r2**2-i**2)
        
        y_min = math.ceil(y_min)
        y_max = math.floor(y_max)
        count += y_max-y_min+1

    count = count*4
    
    return count