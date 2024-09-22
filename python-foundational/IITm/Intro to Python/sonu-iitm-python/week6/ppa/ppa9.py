def get_toppers(scores_dataset , subject , gender):
    gender_filtered=[]
    for key,value in scores_dataset:
        if scores_dataset[gender]==gender:
            gender_filtered.append(key,value)
    highest_data=[]







  #we learned something new known as lambda which is used to check the value of a specific key 
  
  #people = [
    #{'name': 'Alice', 'age': 25},
    #{'name': 'Bob', 'age': 30},
    #{'name': 'Charlie', 'age': 20}
  #] #here we made some data in dictonary  


# Sort by age
#sorted_people = sorted(people, key=lambda person: person['age']) 
#print(sorted_people)



