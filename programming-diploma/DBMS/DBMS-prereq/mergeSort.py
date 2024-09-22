# Notes of merge Sort :- 

'''
    we divide the entire array in half pieces recursively till we get arrays with only 2 members
    then we sort the arrays of length 2 linearly and add the arrays recursively, and then sort the newlyformed array again
'''

def mergeSort (unsortedArray):
    return None


def sortTwoElements(array):
    if array[0] < array[1]:
        return array;
    elif array[0] > array[1]:
        array[0] = array[0] + array[1];
        array[1] = array[0] - array[1];
        array[0] = 