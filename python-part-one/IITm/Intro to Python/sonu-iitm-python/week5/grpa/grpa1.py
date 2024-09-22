list_of_numbers=input().split(',')
str_list_of_numbers = ['1.0', '3.7', '8.9', '5.5', '1.9', '6', '0.1', '9.9']
float_values_of_list=[]
for i in str_list_of_numbers:
    float_values_of_list.append(float(i))

print(float_values_of_list)
maximum_number=[]
for i in float_values_of_list:
    max=float_values_of_list[0]
    for i in float_values_of_list:
        if i>max:
            max=i
    maximum_number.append(max)
    break
print(maximum_number)

minimun_number=[]
for i in float_values_of_list:
    min=float_values_of_list[0]
    for i in float_values_of_list:
        if i<min:
            min=i
    minimun_number.append(min)
    break
print(minimun_number)


def get_range(maximum_number , minimum_number):
  range = maximum_number - minimum_number;
  return (range)

print(get_range(9.9, 0.1))    


 
















#def get_range(float_values_of_list):
