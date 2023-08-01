# Complete the function that accepts a string parameter, and reverses each word in the string. 
# All spaces in the string should be retained.

# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

text = "This is an example!"

def reverse_words(text):

    words = text.split()
    reverse = ""
    text_reversed = []

    for i in words:
        
        reverse = i[::-1]  
        text_reversed.append(reverse)

    return " ".join(text_reversed)

print(reverse_words(text))


# I had some problems with the double spaced words :(