# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

l = [1, -2, 'a', 'b']
new_array = []

for i in l: 
     
     if type(i) != str and i >= 0:
           new_array.append(i)

print(new_array)        
            
