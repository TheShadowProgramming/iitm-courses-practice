n=input().split(',')
int_n=[]
for i in n:
    int_n.append(int(i))
last_list=[]
def first_three(int_n):
    first_max=int_n[0]
    for number in int_n:
        if number>first_max:
            first_max=number
            int_n.remove(number)

    second_max=int_n[0]
    for number in int_n:
        if number==first_max:
            second_max=number
            int_n.remove(number)
        elif number>second_max:
            second_max=number
            int_n.remove(number)

    third_max=int_n[0]
    for number in int_n:
        if number==second_max:
            third_max=number
            int_n.remove(number)
        elif number>third_max:
            third_max=number
            int_n.remove(number)
    return first_max , second_max , third_max

print(first_three(int_n))
