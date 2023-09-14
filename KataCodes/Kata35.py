# Get the Middle Character
# You are going to be given a word. Your job is to return the middle character of the word. 
# If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

# #Examples:
# Kata.getMiddle("test") should return "es"
# Kata.getMiddle("testing") should return "t"
# Kata.getMiddle("middle") should return "dd"
# Kata.getMiddle("A") should return "A"

s = "pampanas"

def get_middle(s):
    new_s = ""
    new_s2 = ""
    if len(s) % 2 == 1:
        # Se o comprimento da string for ímpar, encontre o índice do meio
        new_s = len(s) // 2
        return s[new_s]
    else:
        # Se o comprimento da string for par, encontre os índices do meio
        new_s = len(s) // 2 - 1
        new_s2 = len(s) // 2 + 1
        return s[new_s:new_s2]



print(get_middle(s))