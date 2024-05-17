marks = [30, 40, 50, 10, 20]

sorted_marks = []

while len(marks) > 0:
    min = int(marks[0])
    for i in marks:
        if int(i) < min:
            min = int(i)
    sorted_marks.append(min)
    marks.remove(min)

size = len(sorted_marks)
central_number = size/2
median = 0.0

if size % 2 == 0:
    central_number = int(central_number)
    median = float(
        (sorted_marks[central_number-1]+sorted_marks[central_number])/2
    )
else:
    central_number = int(central_number)
    median = float(sorted_marks[central_number])

print(median)
