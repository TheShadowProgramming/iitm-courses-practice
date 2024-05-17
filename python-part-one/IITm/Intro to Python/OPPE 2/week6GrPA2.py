def freqToWords(ListOfWords):
    setOfWords = set(ListOfWords)
    dic = {}
    for i in setOfWords:
        counter = 0
        for j in ListOfWords:
            if i == j:
                counter += 1
        if counter in dic.keys():
            dic[counter].append(str(i))
        else:
            dic[counter] = []
            dic[counter].append(str(i))
    return dic


ListOfWords = ['a', 'random', 'collection', 'a', 'another', 'a', 'random']
print(freqToWords(ListOfWords))
