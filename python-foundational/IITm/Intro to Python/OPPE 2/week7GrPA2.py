def linear(P, Q, k):
    if P != Q:
        return False
    if len(P) == 0:
        return True
    elif P[0] / Q[0] != k:
        return linear(P[1:], Q[1:], k)
