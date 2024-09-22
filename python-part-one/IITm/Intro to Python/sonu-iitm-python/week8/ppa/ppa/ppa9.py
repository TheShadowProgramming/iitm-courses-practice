def uniq(list):
    if len[list]==1:
        return list
    if list[0]==list[-1]:
        list.remove(list[-1])
    return list[1:] #my code



def uniq(L):
    if len(L) == 1:
        return L
    if L[0] in L[1: ]: #they are simply checking if the first element is in the list or not 
        return uniq(L[1: ])#then simply returning to our old function and removing that first elemnt  
    else:
        return [L[0]] + uniq(L[1: ]) #else we return our checking by adding the first element to the rest list starting from :1 taki wo 0th element last me ajaye
    #iitm code