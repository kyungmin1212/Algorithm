T = input()
n_t = len(T)
P = input()
n_p = len(P)

def make_prefix_next_index(targets):
    prefix_next_index = [0 for _ in range(n_p)]
    
    j = 0
    for i in range(1,n_p):
        while j>0 and targets[i]!=targets[j]:
            j= prefix_next_index[j-1]
        
        if targets[i]==targets[j]:
            j+=1
            prefix_next_index[i] = j
            
    return prefix_next_index

prefix_next_index = make_prefix_next_index(P)

answer = []
count = 0
j = 0
for i in range(n_t):
    while j>0 and T[i]!=P[j]:
        j = prefix_next_index[j-1]
    
    if T[i]==P[j]:
        if j==n_p-1:
            count+=1
            answer.append(i-n_p+2)
            j = prefix_next_index[j]
        else:
            j+=1
print(count)
print(" ".join(map(str,answer)))