def merge( A,B ):
    C = A + B
    a = 0
    b = 0
    for c in range(len(C) - 1):
        print(A[a],B[b])
        #If a is smaller than b, first value is A[a], then increase a
        if A[a] <= B[b]:
            C[c] = A[a]
            a += 1
        #Else first value is B[b], so increase b
        else:
            C[c] = B[b]
            b += 1
    return C

print(merge([2,4,5,7], [1,2,3,6]))

"""
### Algorithm
```
1. While your data set contains more than one item, split it in half
2. Once you have gotten down to a single element, you have also *sorted* that element 
   (a single element cannot be "out of order")
3. Start merging your single lists of one element together into larger, sorted sets
4. Repeat
"""

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
