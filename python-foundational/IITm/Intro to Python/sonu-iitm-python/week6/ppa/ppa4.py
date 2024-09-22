D = {1:10 , 2:10 , 3:10 , 4:10 , 5:10}
value=10





def value_to_keys(D, value):
    values = [ ]
    for key in D:
        if D[key] == value:
            values.append(key)
    return values

print(value_to_keys(D , value))