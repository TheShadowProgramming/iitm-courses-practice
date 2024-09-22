def logarithm(x):
    if x==1:
        return '0'
    if x>1:
        return 1 + logarithm(x//2)