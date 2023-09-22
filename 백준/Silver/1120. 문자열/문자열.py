a,b = input().split()

a_len = len(a)
b_len = len(b)

ans = int(1e9)
for i in range(b_len-a_len+1):
    count=0
    for j in range(a_len):
        if a[j]!=b[i+j]:
            count+=1
    ans=min(ans,count)
print(ans)