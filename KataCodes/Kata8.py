#  Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
# The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). 
# The next words should be always capitalized.

text = "Enzo_garofalo"

def to_camel_case(text):
           
    s = text.replace("-", " ").replace("_", " ")
    s = s.split()
    if len(text) == 0:
        return text
    return s[0] + ''.join(i.capitalize() for i in s[1:])

print(to_camel_case(text))