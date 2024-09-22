space_seperated_words=input('enter your words; ').split()#ham yaha pe user se sentence input krwa rhe h 

word_to_find=input()#yaha ham word ko le rhe h joki hamko check krna hai sentence me 

word_present_or_not = False;

number_of_times=0 #creating a variable to check no. of time it is present
for i in space_seperated_words:
    if word_to_find == i:
        number_of_times+=1
        word_present_or_not = True

if word_present_or_not == True:
    print('YES')
else:
    print('NO')















































print(number_of_times)