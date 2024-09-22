names = input().split(',')
dates = input().split(',')

common = []

n = len(names)

for i in range(n):
    for j in range(n):
        if i != j:
            if dates[i] == dates[j]:
                if names[i] < names[j]:
                    pair = [names[i], names[j]]
                    common.append(pair)
