def total_weight(items):
    weight = 0
    for item in items:
        weight += item[0]
    return weight

def total_value(items):
    value = 0
    for item in items:
        value += item[1]
    return value

def knapsack_greedy(items, max_weight):
    """
    O(n log n) + O(n)
    Not guaranteed to be optimal 

    Args:
        items ([list[tuple]]): list of items; (weight, value)
        max_weight ([int]): max weight that can be carried
    """
    bag_weight = 0
    bag_items = []
    items.sort(reverse=True, key=lambda x: x[1])
    for i in items:
        if max_weight >= bag_weight + i[0]:
            bag_weight += i[0]
            bag_items.append(i)
        if max_weight < bag_weight:
            break
    return bag_items
    


###########################

if __name__ == '__main__':
    items = [ (12,5), (1,6), (1,1), (3,1), (6,4)]
    print(knapsack_greedy(items, max_weight=10))
