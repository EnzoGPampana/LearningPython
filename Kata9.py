# Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. 
# If the two numbers are equal return a or b.
# Note: a and b are not ordered!
a = -1
b = 2

def get_sum(a,b):

    if a == b:
        return a
    elif a > b:
        a, b = b, a


    return sum(range(a , b))


print(get_sum(a, b))