n=input().split(',')
int_n=[]
for i in n:
    int_n.append(int(i))
def maxval(int_n):
    minival=int_n[1]
    for i in int_n:
        if i>=minival:
            minival=i
            return minival

print(maxval(int_n))
