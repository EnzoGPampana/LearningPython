# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
arr = [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]
arr.sort()


for i in arr:
    if i == 0:
       arr.append(i)
       arr.remove(i)
     

print(arr)