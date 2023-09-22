from bisect import bisect_left,bisect_right

n=int(input())

number_list=list(map(int,input().split()))
check=[0]

for number in number_list:
    if check[-1]<number:
        check.append(number)
    else:
        idx=bisect_left(check,number)
        check[idx]=number

print(len(check)-1)