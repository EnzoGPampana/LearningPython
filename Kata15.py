
# Your order, Please
# Your task is to sort a given string. Each word in the string will contain a single number. 
# This number is the position the word should have in the result.
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

sentence = "is2 Thi1s T4est 3a" 

def order(sentence):

    words = sentence.split()
    new_sentence = [''] * len(words)

    for i in words:
        for char in i:
            if char.isdigit():
                position = int(char)
                new_sentence[position - 1] = i            
    
    return " ".join(new_sentence)



print(order(sentence))






