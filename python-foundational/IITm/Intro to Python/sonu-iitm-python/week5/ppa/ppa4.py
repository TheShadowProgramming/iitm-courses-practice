first_matrix=input()

second_matrix=input()

def dim_equal(first_matrix , second_matrix):
    dim1=len(first_matrix)
    dim2=len(second_matrix)
    if dim1==dim2:
        return 'True'
    else:
        return "False"
    
print(dim_equal(first_matrix , second_matrix))