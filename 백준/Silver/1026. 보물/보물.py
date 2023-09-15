n = int(input())

a_arr = list(map(int,input().split()))
b_arr = list(map(int,input().split()))
a_arr = sorted(a_arr)
b_arr = sorted(b_arr,key=lambda x :-x)

s = 0
for i in range(n):
    s+=a_arr[i]*b_arr[i]
    
print(s)