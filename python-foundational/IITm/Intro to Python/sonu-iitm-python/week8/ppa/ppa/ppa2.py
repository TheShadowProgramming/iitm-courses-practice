def factorial(n):
    if n==1 or n==0:
        return '1'
    return n*factorial(n-1) #what's happening here is we are multiplying n with the function factorial n-1 and that"ll go on 
#what exactly is recursion?
# we just write the first step and then tell our computer to go do it wpas se but dont use that 1st inputs
#as here we are going to run the function again but not using the nth number