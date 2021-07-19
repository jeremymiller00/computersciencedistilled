def power_set(s):
  power_set=[[]]
  for elem in s:
    # iterate over the sub sets so far
    for sub_set in power_set:
      # add a new subset consisting of the subset at hand added elem
      power_set=power_set+[list(sub_set)+[elem]]
  return power_set

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

def knapsack_brute_force(items, max_weight):
    """
    O(2**n)

    Args:
        items ([list[tuple]]): list of items; (weight, value)
        max_weight ([int]): max weight that can be carried
    """
    best_value = 0
    best_candidate = None
    for candidate in power_set(items):
        if total_weight(candidate) <= max_weight:
            if total_value(candidate) > best_value:
                best_value = total_value(candidate)
                best_candidate = candidate
    return best_candidate


###########################

if __name__ == '__main__':
    items = [ (12,5), (1,6), (1,1), (3,1) ]
    print(knapsack_brute_force(items, max_weight=10))
