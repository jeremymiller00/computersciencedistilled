""" 
Recursive, and using divide and conquer
"""
from selection_sort import make_array


def trade(prices):
    if len(prices) == 1:
        return 0
    mid_point = len(prices) // 2
    former = prices[:mid_point]
    latter = prices[mid_point:]
    case_3 = max(latter) - min(former)
    return max([trade(former), trade(latter), case_3])


###################

if __name__ == '__main__':
    prices = make_array(100)
    res = trade(prices)
    print(f"Prices: {prices}")
    print(f"Best trade value: {res}")