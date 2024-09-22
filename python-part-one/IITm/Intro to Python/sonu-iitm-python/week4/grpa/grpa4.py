names_of_people=input().split(',')
birthdate_of_people=input().split(',')
int_birthdates_of_people=[]
for birthdates in birthdate_of_people:
    int_birthdates_of_people.append(int(birthdates))
common_birthdate=[]


for i in int_birthdates_of_people:
    if i==int_birthdates_of_people[0]:
        index=int_birthdates_of_people.index
        common_birthdate.append(i)
        common_birthdate.append(int_birthdates_of_people[0])
        #birthdate_of_people.remove(i)
        int_birthdates_of_people.remove(int_birthdates_of_people[0])
print(common_birthdate)

