def find_degree(second):
     
    h = second//3600
    m = second%3600//60
    s = second%3600%60
    h_degree = (h*(360/12)+m*(360/12/60)+s*(360/12/60/60)) % 360
    m_degree = m*(360/60)+s*(360/3600)
    s_degree = s*(360/60)
    
    return h_degree,m_degree,s_degree

def solution(h1, m1, s1, h2, m2, s2):
    start_second = h1*60*60+m1*60+s1
    end_second = h2*60*60+m2*60+s2
    
    answer = 0
    h_d,m_d,s_d = find_degree(start_second)
    if h_d==s_d and m_d==s_d:
        answer+=1
    elif h_d==s_d:
        answer+=1
    elif m_d==s_d:
        answer+=1
        
    for second in range(start_second,end_second):

        h_d,m_d,s_d = find_degree(second)
        next_h_d,next_m_d,next_s_d = find_degree(second+1)

        if (next_h_d==next_s_d) and (next_m_d==next_s_d):
            answer+=1
            continue
        
        if next_s_d==0:
            next_s_d=360
            
        if s_d<h_d and next_h_d<=next_s_d:
            answer+=1
            
        if s_d<m_d and next_m_d<=next_s_d:
            answer+=1

    
    return answer