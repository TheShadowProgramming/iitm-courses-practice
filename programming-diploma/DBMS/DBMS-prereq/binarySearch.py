def binarySearch (sortedArray, valueToSearch):
    middle = len(sortedArray) // 2;

    if valueToSearch < sortedArray[middle]:
        sortedArray = sortedArray[:middle];
        return binarySearch (sortedArray, valueToSearch)
    elif valueToSearch > sortedArray[middle]:
        sortedArray = sortedArray[middle:];
        return binarySearch (sortedArray, valueToSearch)
    else:
        l
        