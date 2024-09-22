n=int(input())




list_of_students=[]



for i in range(n):
    dict={}
    dict['name']=input()
    dict['city']=input()
    dict['seqno.']=input()
    dict['maths']=input()
    dict['physics']=input()
    dict['chemistry']=input()
    list_of_students.append(dict)

print(list_of_students)