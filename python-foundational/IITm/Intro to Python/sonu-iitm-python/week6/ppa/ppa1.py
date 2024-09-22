#
freq = dict()
L = input().split(',')

for word in L:
    freq[word] = 0 #here we are saying that value is 0 of everything that is in L

for word in L:
    freq[word] = freq[word] + 1

print(freq)