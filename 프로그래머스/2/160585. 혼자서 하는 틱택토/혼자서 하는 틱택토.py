def solution(board):
    o_count=0
    x_count=0
    for row in range(3):
        for column in range(3):
            if board[row][column]=="O":
                o_count+=1
            elif board[row][column]=='X':
                x_count+=1
    # X가 더많은 경우
    if x_count>o_count:
        return 0
    # O가 두개이상 더많은경우
    if x_count+2<=o_count:
        return 0
        
    # O 3개가 완성됐는데 O랑 X개수가 같은 경우
    # 3개가 완성될 경우 row로 ooo, column으로 ooo, 양쪽 대각선 ooo   
    o_complete_flag = False
    for column in range(3):
        flag = True
        for row in range(3):
            if board[row][column]=="X" or board[row][column]==".":
                flag = False
                break
        if flag:
            o_complete_flag = True
            break
    
    for row in range(3):
        flag = True
        for column in range(3):
            if board[row][column]=="X" or board[row][column]==".":
                flag=False
                break
        if flag:
            o_complete_flag = True
            break
    
    flag=True
    for i in range(3):
        if board[i][i]=="X" or board[i][i]==".":
            flag=False
            break
    if flag:
        o_complete_flag=True
    
    flag=True
    for i in range(3):
        if board[i][2-i]=="X" or board[i][2-i]==".":
            flag=False
            break
    if flag:
        o_complete_flag=True

    # X가 완성된경우
    x_complete_flag = False
    for column in range(3):
        flag = True
        for row in range(3):
            if board[row][column]=="O" or board[row][column]==".":
                flag = False
                break
        if flag:
            x_complete_flag = True
            break
    
    for row in range(3):
        flag = True
        for column in range(3):
            if board[row][column]=="O" or board[row][column]==".":
                flag=False
                break
        if flag:
            x_complete_flag = True
            break
    
    flag=True
    for i in range(3):
        if board[i][i]=="O" or board[row][column]==".":
            flag=False
            break
    if flag:
        x_complete_flag=True
    
    flag=True
    for i in range(3):
        if board[i][2-i]=="O" or board[row][column]==".":
            flag=False
            break
    if flag:
        x_complete_flag=True
        
    if o_complete_flag:
        if o_count==x_count:
            return 0
        
    if x_complete_flag:
        if x_count+1<=o_count: # x가 완성상태인데 o개수가 x보다 1개이상 많을경우
            return 0
    return 1