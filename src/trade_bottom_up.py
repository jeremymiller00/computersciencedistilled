""" 
Bottom up, dunamic programming
O(n)
"""
from selection_sort import make_array


def trade_bu(prices):
    B = {}
    B[1] = 1
    sell_day = 1
    best_profit = 0

    for n in range(2, len(prices)):
        if prices[n] < prices[B[n-1]]:
            B[n] = n
        else:
            B[n] = B[n-1]
        profit = prices[n] - prices[B[n]]
        if profit > best_profit:
            sell_day = n
            best_profit = profit
    
    return sell_day, B[sell_day]


###################

if __name__ == '__main__':
    prices = make_array(100)
    sell_day, buy_day = trade_bu(prices)
    best_profit = prices[sell_day] - prices[buy_day]
    print(f"Prices: {prices}")
    print(f"Best trade value: {best_profit}")