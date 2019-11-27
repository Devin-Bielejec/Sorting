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
def swap(index1, index2, li):
    temp = li[index1]
    li[index1] = li[index2]
    li[index2] = temp
    return li


def insertionSort(A):
    for index1 in range(1, len(A)):
        for index2 in range(index1-1, -1, -1):
            if A[index1] < A[index2]:
                #swap items
                swap(index1, index2, A)
                #Reduce index1 by 1 because it has moved to the left
                index1 -= 1
            else:
                break 
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
def selection_sort(A):
    #Loop through all but last element
    for index1 in range(len(A)-1):
        indexMin = index1
        for index2 in range(index1, len(A)):
            if A[index2] < A[indexMin]:
                indexMin = index2
        #Swap current elemtn with smallest element
        if A[index1] > A[indexMin]:
            swap(index1, indexMin, A) 
    return A



print(selection_sort([14, 6, 3, 5, 32, -1, -2, 4, 10 , 2]))

"""
### Algorithm
1. Loop through your array
    - Compare each element to its neighbor
    - If elements in wrong position (relative to each other, swap them)
2. If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
"""


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(A):
    count = 1
    while count > 0:
        print(A)
        count = 0
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                swap(i, i+1, A)
                count += 1
    return A    
    

print("bubble",bubble_sort([3,2,1]))



# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr