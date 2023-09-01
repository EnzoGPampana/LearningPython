# Consecutive strings
# You are given an array(list) strarr of strings and an integer k. 
# Your task is to return the first longest string consisting of k consecutive strings taken in the array.
# strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2
# treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
# abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]
# Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
# The first that came is "folingtrashy" so 
# longest_consec(strarr, 2) should return "folingtrashy".

strarr = ["enzo", "garofalo", "pampana", "big", "poppa", "ice"]
k = 2

def longest_consec(strarr, k):
    concatenated_strings = []
    n = len(strarr)
    
    if n == 0 or k > n or k <= 0:
        return ""
    
    for i in range(n - k + 1):
        current_string = "".join(strarr[i:i+k])
        concatenated_strings.append(current_string)
    return max(concatenated_strings, key=len)

print(longest_consec(strarr, k))