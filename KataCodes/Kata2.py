#Return the number (count) of vowels in the given string.
#We will consider a, e, i, o, u as vowels for this Kata (but not y).
#The input string will only consist of lower case letters and/or spac

vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
string = "ENZoooooooooooooooooooiiiiiiiiiieeeeeeeeeeeaaaaaaaaaO"    
n = 0

for i in string: 

    if i in vowels:
        n += 1

print(n)       
