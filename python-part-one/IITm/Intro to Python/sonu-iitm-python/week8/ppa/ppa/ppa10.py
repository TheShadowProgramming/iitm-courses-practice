def search(list , k):
    if len[list]==1:
        return list
    if list[0]==k:
        return 'True'
    return search(list[1:] , k)
    
