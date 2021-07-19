def power_set(s):
  power_set=[[]]
  for elem in s:
    # iterate over the sub sets so far
    for sub_set in power_set:
      # add a new subset consisting of the subset at hand added elem
      power_set=power_set+[list(sub_set)+[elem]]
  return power_set


##########################

if __name__ == '__main__':
    s1 = [1,2,3,4]
    print("Power Set")
    print(power_set(s1))