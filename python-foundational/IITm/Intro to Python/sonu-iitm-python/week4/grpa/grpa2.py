input_of_marks = input().split(',')
int_input_of_marks = []

for str_int in input_of_marks:
    int_input_of_marks.append(int(str_int))

even_list_of_input = []
odd_list_of_input = []

if len(int_input_of_marks) % 2 == 0:
    even_list_of_input = int_input_of_marks
elif len(int_input_of_marks) % 2 == 1:
    odd_list_of_input = int_input_of_marks


sorted_even_list_of_input=[]
sorted_odd_list_of_input=[]

for i in range(0, len(even_list_of_input)):
    min = 10000
    for memberof1list in even_list_of_input:
        if memberof1list<=min:
            min=memberof1list
    sorted_even_list_of_input.append(min)
    even_list_of_input.remove(min)
        
for i in range(0, len(odd_list_of_input)):
    min = 10000
    for memberoflist in odd_list_of_input:
        if memberoflist<min:
            min=memberoflist
    sorted_odd_list_of_input.append(min)    
    odd_list_of_input.remove(min)


for mediano in range(0,len(sorted_odd_list_of_input)) :
    mediano=sorted_odd_list_of_input[len(sorted_odd_list_of_input)//2]
    print(mediano)


for mediane in range(0,len(sorted_even_list_of_input)):
    mediane=(sorted_even_list_of_input[len(sorted_even_list_of_input)//2] + sorted_even_list_of_input[len(sorted_even_list_of_input)//2-1])//2

print(mediane)