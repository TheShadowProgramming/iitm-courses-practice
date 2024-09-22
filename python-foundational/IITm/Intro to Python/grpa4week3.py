n = str(input())

n = n.lower()

alpha = 'abcdefghijklmnopqrstuvwxyz'
sortedlist = []
i = 0
while i < 26:
    for j in range(len(n)):
        if n[j] == alpha[i]:
            sortedlist.append(n[j])
    i += 1

for i in range(len(sortedlist)):
    print(sortedlist[i], end='')
