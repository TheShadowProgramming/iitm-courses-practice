number_to_add_x=int(input())

list_of_number = input().split(',')
int_list_of_number = []
for i in list_of_number:
    int_list_of_number.append(int(i))

sorted_list_of_number = []

for i in range(0, len(int_list_of_number)): 
    min=int_list_of_number[0]
    for i in int_list_of_number:
        if i<=min:
            min=i

    int_list_of_number.remove(min)
    sorted_list_of_number.append(min)
#print(sorted_list_of_number)
#sorting funtion, we are running a loop on our integer list in which we are setting the minimum value as the first 
#element then we are checking if there's any other element in our int list by adding one more for loop and then if 
#there's any other elemnet smaller than it we'll make that our smallest element by doing this we'll append our smallest
#element to our new list and following all the other numbers  

def insert11(sorted_list_of_number , number_to_add_x):
    new_sorted_list=[]
    if number_to_add_x==0:
        sorted_list_of_number[0]=number_to_add_x
        return sorted_list_of_number
    if number_to_add_x==1:
        sorted_list_of_number[1]=number_to_add_x
        return sorted_list_of_number
    if number_to_add_x>1:
        sorted_list_of_number.append(number_to_add_x)
    for i in sorted_list_of_number:
        min1=sorted_list_of_number[0]
        for i in sorted_list_of_number:
            if i<=min1:
                min1=i
        new_sorted_list.append(min1)
        sorted_list_of_number.remove(min1)
        return new_sorted_list



print(insert11(sorted_list_of_number , number_to_add_x))
