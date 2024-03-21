def solution(friends, gifts):
    friends_idx = {name:i for i,name in enumerate(friends)}
    
    gift_count = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    total_gift_count = [0 for _ in range(len(friends))]
    
    for name in gifts:
        a,b = name.split(" ")
        a_idx = friends_idx[a]
        b_idx = friends_idx[b]
        total_gift_count[a_idx]+=1
        total_gift_count[b_idx]-=1
        gift_count[a_idx][b_idx]+=1
        
        
    max_count=0

    for i in range(len(friends)):
        count = 0
        for j in range(len(friends)):
            if i==j:
                continue
            if gift_count[i][j]>gift_count[j][i]:
                count+=1
            elif gift_count[i][j]==gift_count[j][i]:
                if total_gift_count[i]>total_gift_count[j]:
                    count+=1
        max_count = max(max_count,count)
    
    return max_count
