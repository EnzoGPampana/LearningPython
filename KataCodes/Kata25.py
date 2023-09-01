# Given an array of integers, return a new array with each value doubled.
# For example:
# [1, 2, 3] --> [2, 4, 6]

a =  [2, 4, 6]

def maps(a):
    new_a = []

    for i in a:
        new_a.append(i*2)
    return new_a


print(maps(a))