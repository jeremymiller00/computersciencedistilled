""" 
Knapsack problem with divide and conquer method

"""

class Item:
    def __init__(self, w=None, v=None):
        super().__init__()
        self.w = w
        self.v = v
    
    def setWeight(self, w):
        self.w = w

    def setValue(self, v):
        self.v = v

    def getWeight(self):
        return self.w

    def getValue(self):
        return self.v


def K(items):
    if len(items) == 1:
        return 0
    mid_point = len(items) // 2
    former = items[:mid_point]
    latter = items[mid_point:]
    case_3 = max(latter) - min(former)
    return max([K(former), K(latter), case_3])

""" 
class Knapsack:
    def __init__(self, capacity=None, items=None):
        super().__init__()
        self.capacity = capacity
        self.items = items

    def K(self, items):
        current_value = sum([i.v for i in items])
        return max(K())


def totalWeight(items):
    return sum([i.w for i in items])        

def totalValue(items):
    return sum([i.v for i in items])        

def optimize(items, capacity):
    n = len(items)
    if n == 0:
        return 0
    return max(optimize(items[:-1], capacity),
               optimize(items[:-1], capacity - items[-1].w))
"""

#########################

if __name__ == '__main__':
    assert totalWeight( [Item(1,2), Item(4,8), Item(2,1)] ) == 7
    assert totalValue( [Item(1,2), Item(4,8), Item(2,1)] ) == 11