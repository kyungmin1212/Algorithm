d = int(input())

arr = [[0,1,1,0,0,0,0,0],
       [1,0,1,1,0,0,0,0],
       [1,1,0,1,1,0,0,0],
       [0,1,1,0,1,1,0,0],
       [0,0,1,1,0,1,1,0],
       [0,0,0,1,1,0,0,1],
       [0,0,0,0,1,0,0,1],
       [0,0,0,0,0,1,1,0]]

def matrix_dot(a,b):
    a_row= len(a)
    a_column = len(a[0])

    b_row = len(b)
    b_column = len(b[0])

    new_arr = [[0 for _ in range(b_column)] for _ in range(a_row)]

    for r in range(a_row):
        for c in range(b_column):
            v = 0
            for m in range(a_column):
                v+=((a[r][m]%1000000007)*(b[m][c]%1000000007))%1000000007
            new_arr[r][c]= v%1000000007

    return new_arr

def matrix_n_squre(arr,n):
    if n==1:
        return arr

    if n%2==0:
        sub_arr = matrix_n_squre(arr,n//2)
        return matrix_dot(sub_arr,sub_arr)
    elif n%2==1:
        sub_arr = matrix_n_squre(arr,n//2)
        return matrix_dot(matrix_dot(sub_arr,sub_arr),arr)
    
print(matrix_n_squre(arr,d)[0][0])