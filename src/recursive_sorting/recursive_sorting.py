# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    arrA.append(float("inf"))
    arrB.append(float("inf"))
    for i in range(elements):
        if arrA[0] <= arrB[0]:
            merged_arr[i] = arrA[0]
            arrA.pop(0)
        else:
            merged_arr[i] = arrB[0]
            arrB.pop(0)
    return merged_arr

"""
1. While your data set contains more than one item, split it in half
2. Once you have gotten down to a single element, you have also *sorted* that element 
   (a single element cannot be "out of order")
3. Start merging your single lists of one element together into larger, sorted sets
4. Repeat step 3 until the entire data set has been reassembled
"""

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    #chicken
    if len(arr) == 0:
        return arr
    # TO-DO
    if len(arr) == 1:
        return arr
    else: 
        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]
        return merge(merge_sort(left),merge_sort(right))
        
