def get_marks(scores_dataset , subject): #we took two arguements one being data set and other being the subject of which marks we want
    L=[]#we created a list to append the name and marks of the desired subject we want
    for student in scores_dataset: #we are iterating in scores dataset dictonary with the variable student
        marks=student[subject] #here the student will iterate over all the keys in the dictnoary and when he will get the specified subjects he will take the value of that subject key and store it inside in marks
        name=student['Name'] # here we are simply going further and taking the 'name' key's value and appending it to name variable 
        L.append((name , marks))
        return L