def multiply(a , b):
    if b==1:
        return a
    if b>1:
        return a + multiply(a , b-1)
    