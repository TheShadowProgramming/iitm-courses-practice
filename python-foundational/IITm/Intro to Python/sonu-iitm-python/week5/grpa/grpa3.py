


def distance(word_1, word_2):
    # first condition
    if len(word_1) != len(word_2):
        return -1
    letters = 'abcdefghijklmnopqrstuvwxyz'
    size = len(word_1)
    dist = 0
    for i in range(size):
        c1, c2 = word_1[i], word_2[i]
        # distance between letters
        d = abs(letters.index(c1) - letters.index(c2))  #index gives us the position of the 1st letter in the list of alphabet list 
        dist += d
    return dist