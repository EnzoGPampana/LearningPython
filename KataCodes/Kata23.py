# Tribonacci Sequence
# you need to create a fibonacci function that given a signature array/list, 
# returns the first n elements - signature included of the so seeded sequence.
# Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, 
# then return an empty array (except in C return NULL) and be ready for anything else which is not clearly specified ;)

signature = [1, 1, 1]
n = 2

def tribonacci(signature, n):

    if n == 0:
        return []
    elif n < 3:
        return signature[:n]

    
    sequence = signature.copy()

    for i in range(n):
        next_element = sequence[i - 1] + sequence[i - 2] + sequence[i-3]
        sequence.append(next_element)
    
    return sequence


print(tribonacci(signature, n))