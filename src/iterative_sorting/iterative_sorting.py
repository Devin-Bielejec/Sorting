#Insertion Sort
"""
### Algorithm
1. Separate the first element from the rest of the array. Think about it as a sorted list of one element.

2. For all other indices, beginning with [1]:

    a. Copy the item at that index into a temp variable

    b. Iterate to the left until you find the correct index in the "sorted" part of the array at which this element should be inserted  
    - Shift items over to the right as you iterate
    
    c. When the correct index is found, copy temp into this position
"""

def insertionSort(A):
    for i in range(1, len(A)):
        cur = A[i]
        j = i - 1
        while A[j] > cur and j >= 0:
            #since prev value is larger, prev = cur
            A[j+1] = A[j]
            #Previous index decreases by 1
            j = j - 1
        #Set 
        A[j+1] = cur
    return A

print(insertionSort([5,3,2,1]))

"""
### Algorithm
1. Start with current index = 0

2. For all indices EXCEPT the last index:

    a. Loop through elements on right-hand-side 
    of current index and find the smallest element

    b. Swap the element at current index with the
    smallest element found in above loop
"""



# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i, len(arr)):
            if (arr[j] < arr[smallest_index]):
                smallest_index = j 

        # TO-DO: swap
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp
    return arr

print(selection_sort([10,9,8, -1, 15, 3, 2]))
# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr