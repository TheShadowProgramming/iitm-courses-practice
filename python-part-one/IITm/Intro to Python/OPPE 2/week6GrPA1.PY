# We have to iterate through the dictionary and select specific gender and specific subject
# we'll first maintain max and update it during the iteration
# after this, whoever has the max marks will be appended in the list

def getToppers(scoresDataSet, subject, gender):
    max = 0
    toppersList = []
    for i in scoresDataSet:
        if i['Gender'] == gender and i[subject] > max:
            max = i[subject]
            toppersList = []
            toppersList.append(i['Name'])
        elif i['Gender'] == gender and i[subject] == max:
            toppersList.append(i['Name'])
    return toppersList


L = [
    {'SeqNo': 1, 'Name': 'Devika', 'Gender': 'F', 'City': 'Bengaluru',
     'Mathematics': 64, 'Physics': 48, 'Chemistry': 79, 'Biology': 75,
     'Computer Science': 88, 'History': 43, 'Civics': 78, 'Philosophy': 55},
    {
        'SeqNo': 2, 'Name': 'Mayank', 'Gender': 'M', 'City': 'Bengaluru',
        'Mathematics': 64, 'Physics': 48, 'Chemistry': 79, 'Biology': 75,
        'Computer Science': 88, 'History': 43, 'Civics': 78, 'Philosophy': 75
    },
    {
        'SeqNo': 1, 'Name': 'Monish', 'Gender': 'M', 'City': 'Bengaluru',
        'Mathematics': 64, 'Physics': 48, 'Chemistry': 79, 'Biology': 75,
        'Computer Science': 88, 'History': 43, 'Civics': 78, 'Philosophy': 85
    },
    {
        'SeqNo': 1, 'Name': 'Harsh', 'Gender': 'M', 'City': 'Bengaluru',
        'Mathematics': 64, 'Physics': 48, 'Chemistry': 79, 'Biology': 75,
        'Computer Science': 88, 'History': 43, 'Civics': 78, 'Philosophy': 85
    }
]
print(getToppers(L, 'Philosophy', 'M'))
