# # You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or
# # entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
integers = [160, 3, 1719, 19, 11, 13, -21]
def find_outlier(integers):
   
    odd = []
    even = []

    for i in integers:
        if i % 2 == 0:
              even.append(i)
        elif i % 2 != 0:
              odd.append(i)

    num = 0
    if len(odd) == 1:
        num = odd[0]
        return num 
    else:
        num = even[0]
        return num    
                  
print(find_outlier(integers))