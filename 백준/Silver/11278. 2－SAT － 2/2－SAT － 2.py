from itertools import product
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

check_list = product((True,False),repeat=n)

m_list = [list(map(int,input().split())) for _ in range(m)]

flag = False
for check in check_list:
    sub_flag = True
    for m in m_list:
        a,b = m
        if a>0:
            check_a = check[a-1]    
        else:
            check_a = not check[-a-1]
        if b>0:
            check_b = check[b-1]
        else:
            check_b = not check[-b-1]
        if check_a or check_b:
            continue
        else:
            sub_flag = False
            break
    if sub_flag:
        print(1)
        for c in check:
            if c ==True:
                print(1,end=' ')
            else:
                print(0,end=' ')
        flag = True
        break
if not flag:
    print(0)