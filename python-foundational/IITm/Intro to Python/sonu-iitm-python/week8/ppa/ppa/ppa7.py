def count(list , word):
    if len[list]==0:
        return 0
    if list[0]==word:
        return 1 + count(list[1:] , word)
    else:
        return count(list[1:] , word)