import sys
import random
from time import time

from selection_sort import selection_sort, make_array
from merge_sort import merge, merge_sort


def compare(algos=["merge_sort", "selection_sort"], arr_size=20000):
    arr = make_array(arr_size)
    result = {}
    algo_dict = {"merge_sort": merge_sort, "selection_sort": selection_sort}
    for algo in algos:
        start = time()
        alg = algo_dict.get(algo)
        res = alg(arr)
        end = time()
        result[algo] = f"{algo} processed {arr_size} items in {end-start} seconds"
    return result




######################

if __name__ == '__main__':
    res = compare()