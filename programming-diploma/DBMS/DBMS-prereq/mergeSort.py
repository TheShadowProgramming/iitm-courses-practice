def mergeInSortedManner (left, right):

    i, j = 0, 0;
    mergedSortedArray = [];

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            mergedSortedArray.append(left[i]);
            i += 1;
        else:
            mergedSortedArray.append(right[j]);
            j += 1;

    while i < len(left):
        mergedSortedArray.append(left[i]);
        i += 1;

    while j < len(right):
        mergedSortedArray.append(right[j])
        j += 1;

    return mergedSortedArray;

def mergeSort (unsortedArray):

    if len(unsortedArray) == 1:
        return unsortedArray; # already sorted

    middle = len(unsortedArray) // 2;
    firstHalf = unsortedArray[:middle];
    secondHalf = unsortedArray[middle:];

    firstBrokenHalf = mergeSort(firstHalf);
    secondBrokenHalf = mergeSort(secondHalf);

    return mergeInSortedManner(firstBrokenHalf, secondBrokenHalf);

strUnsortedArray = input("Enter the stringified array here:").split(",");
unsortedArray = []
i = 0;
while i < len(strUnsortedArray):
    unsortedArray.append(int(strUnsortedArray[i]))
    i += 1;

print(mergeSort(unsortedArray));