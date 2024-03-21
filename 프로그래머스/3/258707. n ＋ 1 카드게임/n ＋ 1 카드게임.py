from heapq import heappush,heappop

def solution(coin, cards):

    n = len(cards)
    q=[]
    turn_cards = []
    for i in range(n):
        if i<n//3:
            turn_cards.append(0)
        else:
            turn_cards.append((i-n//3)//2+1)
    
    check_flag = [False for _ in range(n)]
    for i in range(n):
        if check_flag[i]:
            continue
        check_flag[i]=True
        value = cards[i]
        diff_value = n+1-value
        diff_idx = cards.index(diff_value)
        check_flag[diff_idx]=True
        turn_cards[i]=max(turn_cards[i],turn_cards[diff_idx])
        if i<n//3 and diff_idx<n//3:
            heappush(q,(turn_cards[i],0))
        elif i<n//3 and diff_idx>=n//3:
            heappush(q,(turn_cards[i],1))
        else:
            heappush(q,(turn_cards[i],2))
            
    round = 0
    
    while True:
        round += 1
        if round==(n//3+1):
            break
            
        while q[0][0]<round:
            t,f=heappop(q)
            heappush(q,(round,f))
        
        turn,flag = heappop(q)
        
        if turn>round:
            break
        else:
            coin = coin-(flag)
            if coin<0:
                break

    return round