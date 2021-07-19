# merge two sorted arrays

from time import time
import random
import sys



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



####

if __name__ == '__main__':
    arr1 = ['cod', 'herring', 'marlin']
    arr2 = ['asp', 'carp', 'ide', 'trout']
    res = ['asp', 'carp', 'cod', 'herring', 'ide', 'marlin', 'trout']
    assert(merge(arr1, arr2) == res)