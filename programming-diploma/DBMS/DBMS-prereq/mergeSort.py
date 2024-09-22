# Notes of merge Sort :- 

'''
    we divide the entire array in half pieces recursively till we get arrays with only 2 members
    then we sort the arrays of length 2 linearly and add the arrays recursively, and then sort the newlyformed array again
'''

unsortedArray = input('enter the unsorted array in form of string here');

def sortTwoElements(array):
    if (array[0] < array[1]) or (array[0] == array[1]):
        return array;
    elif array[0] > array[1]: # works for numbers only, well this sorting algorithm only makes sense under the sorting context
        array[0] = array[0] + array[1];
        array[1] = array[0] - array[1];
        array[0] = array[0] - array[1];

def mergeSort (unsortedArray):
    if len(unsortedArray) == 2:
        return sortTwoElements(unsortedArray)
    middleIndex = len(unsortedArray) // 2
    return None;