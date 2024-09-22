import math
n = int(input())

coordinates_list = []

for i in range(n):
    coordinates = input().split(',')
    coordinates_list.append(coordinates)

PointP = input().split(',')


def distance(x, y):
    distn = math.sqrt(
        (int(x[0])-int(y[0]))**2 +
        (int(x[1])-int(y[1]))**2
    )
    return distn


for i in range(n):
    mindistance = distance(PointP, coordinates_list[0])
    for j in coordinates_list:
        if distance(PointP, j) < mindistance:
            mindistance = distance(PointP, j)
