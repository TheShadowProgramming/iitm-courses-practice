def mini(L):
    mini = L[0]
    for i in L:
        if i < mini:
            mini = i
    return mini


def recursiveSort(L):
    if len(L) == 0 or len(L) == 1:
        return L
    m = mini(L)
    L.remove(m)
    return [m]+recursiveSort(L)


L = [3, 4, 6, 7, 8]
print(recursiveSort(L))
