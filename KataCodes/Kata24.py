# Square(n) Sum
# Complete the square sum function so that it squares each number passed into it and then sums the results together.
# For example, for [1, 2, 2] it should return 9 

numbers = []

def square_sum(numbers):

    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i]**2
    return total


print(square_sum(numbers))