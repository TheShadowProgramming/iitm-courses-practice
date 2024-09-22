#n=int(input())

def factors(n):
    F = set()
    for i in range(1, n + 1): #we are doing this range because we need to iterate from 1 to the actual value of n/input if we just do range(n) then it will just iterate till second last value
        if n % i == 0:
            F.add(i)
    return F
#a=int(input())
#b=int(input())
def common_factors(a , b):
    
    factora=factors(a)
    factorb=factors(b)
    return factora.intersection(factorb)

#print(common_factors(a , b))
n=int(input())
def factors_upto(n):
    dict={}
    for i in range(1 , n+1):
        dict[i]=factors(i)
    return dict
    
print(factors_upto(n))