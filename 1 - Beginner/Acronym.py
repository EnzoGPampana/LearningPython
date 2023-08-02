# Acronym
# An acronym is a short form of a word created by long words or phrases such as NLP for natural language processing

phrase = str(input("Digite Uma frase: "))

def acronym(phrase):

    acr = " "
    text = phrase.split()
    for i in text:
        acr= acr+str(i[0]).upper()
    return acr

print(acronym(phrase))