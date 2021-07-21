# simple selection sort algorithm
# Big-O == O(n**2)

from time import time
import random
import sys

def make_array(n: int) -> list:
    return [random.randint(0, 1000) for i in range(n)]

def swap_items(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def selection_sort(arr: list) -> list:
    for current in range(0, len(arr)):
        smallest = current
        for i in range(current + 1, len(arr)):
            if arr[i] < arr[smallest]:
                smallest = i
        swap_items(arr, current, smallest)

def growth(sizes=[10,100,1000,10000,100000], maxi=1000000):
    for s in sizes:
        if s <= maxi:
            start = time()
            res = make_array(s)
            selection_sort(res)
            end = time()
            print(f"\n{s} items sorted in {end - start} seconds\n")

###################

if __name__ == '__main__':
    if len(sys.argv) > 1:
        maxi = sys.argv[1]
        growth(maxi=maxi)
    else:
        growth()