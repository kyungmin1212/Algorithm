def solution(picks, minerals):
    
    n_picks = sum(picks)
    
    minerals = minerals[:5*n_picks]
    
    sub_minerals=[]
    sub_counts =[]
    
    mine=[]
    idx=0
    counts=[0,0,0,idx]
    
    for i in range(len(minerals)):
        mine.append(minerals[i])
        if minerals[i]=="diamond":
            counts[0]+=1
        elif minerals[i]=="iron":
            counts[1]+=1
        elif minerals[i]=='stone':
            counts[2]+=1
        
        if (i+1)%5==0:
            sub_minerals.append(mine)
            sub_counts.append(counts)
            mine=[]
            idx+=1
            counts=[0,0,0,idx]
    if (i+1)%5!=0:
        sub_minerals.append(mine)
        sub_counts.append(counts)
          
    sub_counts.sort(key=lambda x:(-x[0],-x[1],-x[2]))
    
    len_sub_counts = len(sub_counts)
    idx = 0
    answer = 0
    for i,pick in enumerate(picks):
        check_pick = pick
        while check_pick>0 and idx<len_sub_counts:
            if i==0:
                answer+=1*sub_counts[idx][0]+1*sub_counts[idx][1]+1*sub_counts[idx][2]
            elif i==1:
                answer+=5*sub_counts[idx][0]+1*sub_counts[idx][1]+1*sub_counts[idx][2]
            elif i==2:
                answer+=25*sub_counts[idx][0]+5*sub_counts[idx][1]+1*sub_counts[idx][2]
            
            check_pick-=1
            idx+=1
                 
    return answer