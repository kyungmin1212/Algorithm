a, b = map(int,input().split())

dp = [0,1]

before_value = 1
for i in range(1,55):
    now_value = 2**i+before_value
    dp.append(now_value)
    before_value = now_value+before_value

bin_a = bin(a)[2:]
bin_b = bin(b)[2:]

len_a = len(bin_a)
len_b = len(bin_b)

a_count = 0
one_count = 0
for i in range(len_a):
    if bin_a[i]=='1':
        a_count += sum(dp[:len_a-i]) + one_count*(2**(len_a-(i+1)))
        one_count+=1

b_count=0
one_count = 0
for i in range(len_b):
    if bin_b[i]=='1':
        b_count += sum(dp[:len_b-i]) + one_count*(2**(len_b-(i+1)))
        one_count+=1

print(b_count+sum(map(int,list(bin_b))) - a_count)