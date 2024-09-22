n=int(input())

def checkleapyear(n):
    if n%4==0:
        return 'true'
    if n%4!=0:
        return 'false'
    
print(checkleapyear(n))