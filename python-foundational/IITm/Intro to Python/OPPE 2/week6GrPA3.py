def rotateMat(mat):
    orderR = len(mat)
    orderC = len(mat[0])
    transposeMat = []
    for i in range(orderC):
        transposeMat.append([])
    for i in range(orderR):
        for j in range(orderC):
            transposeMat[j].append(mat[i][j])
    for i in range(len(transposeMat)):
        transposeMat[i].reverse()
    return transposeMat


Mat = [
    [1, 2],
    [3, 4],
    [5, 6]
]

print(Mat)
print(rotateMat(Mat))
