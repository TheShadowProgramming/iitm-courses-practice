n = int(input())

A = []
B = []

for i in range(n):
    A.append([])
    input_rowA = input()
    for j in input_rowA.split(','):
        A[i].append(int(j))

for i in range(n):
    B.append([])
    input_rowB = input()
    for j in input_rowB.split(','):
        B[i].append(int(j))

A_prod_B = []

for i in range(n):
    A_prod_B.append([])
    for j in range(n):
        A_prod_B[i].append(0)

for i in range(n):
    for j in range(n):
        element_prod = 0
        for k in range(n):
            element_prod += A[i][k]*B[k][j]
        A_prod_B[i][j] = element_prod

for i in range(n):
    for j in range(n):
        if j != n-1:
            print(A_prod_B[i][j], end=',')
        else:
            print(A_prod_B[i][j])
