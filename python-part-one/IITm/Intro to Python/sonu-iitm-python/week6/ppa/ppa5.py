D = {'abc':3  , 'def':10}

#def dict_to_list(D):
    #L = [ ]

    #for key in D:
        #L.append((key, D[key]))

    #return L
#print(dict_to_list(D))
L= [('def', 10), ('abc', 3)]

def list_to_dict(L):
    dict = {}
    L= [('def', 10), ('abc', 3)] 
    for key,value in L:
        dict[key]=value #here we are adding the key in the dict by making their value equal to value that is in the list
        return dict
print(list_to_dict(L))





