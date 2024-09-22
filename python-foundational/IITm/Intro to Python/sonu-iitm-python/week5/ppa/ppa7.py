numbers=input()

def is_empty(numbers):
    if numbers==[]:
        return 'True'
    else:
        return 'False'
    
def first(numbers):
    if numbers!=[]:
        return numbers[0]
    else:
        return 'none'

def last(numbers):
    if numbers!=[]:
        return numbers[-1]
    else:
        return 'None'
    
def init(numbers):
    if numbers==[]:
        return 'None'
    if len(numbers)==1:
        return []
    else:
        return numbers[:-1]
    
def rest(numbers):
    if numbers==[]:
        return 'None'
    if len(numbers)==1:
        return []
    else:
        return numbers[1:]    
    
#print(is_empty(numbers))
#print(first(numbers))
#print(last(numbers))
#print(init(numbers))    
#print(rest(numbers))