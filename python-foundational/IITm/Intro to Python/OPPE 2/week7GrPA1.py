def reverse(L):
    if len(L) == 1:
        return L
    else:
        return ([L[-1]] + (reverse(L[: -1])))
