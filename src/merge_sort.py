""" 
Merge sort algorithm
O(n log n)
"""

def merge(arr1, arr2):
    result = []
    while len(arr1) != 0 and len(arr2) != 0:
        if arr1[0] < arr2[0]:
            item = arr1.pop(0)
        else:
            item = arr2.pop(0)
        result.append(item)
    if len(arr1) != 0:
        result.extend(arr1)
    elif len(arr2) != 0:
        result.extend(arr2)
    return result

def merge_sort(l):
    if len(l) == 1:
        return l
    mid_point = len(l) // 2
    left = l[:mid_point]
    right = l[mid_point:]
    return merge(merge_sort(left), merge_sort(right))


##########################

if __name__ == '__main__':
    l = [27,53,7,25,33,2,32,47,43]
    res = merge_sort(l)