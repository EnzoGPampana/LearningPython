# Deoxyribonucleicacid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms. 
# If you want to know more: http://en.wikipedia.org/wiki/DNA
# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); 
# you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).


dna = "ATTGC"

def DNA_strand(dna):
    arrDNA = []
    arrDNA = dna
   
    matchDNA = ""

    for i in arrDNA:

        if i == "A":
            matchDNA += "T"

        elif i == "T":
            matchDNA += "A"

        elif i == "G":
             matchDNA += "C"

        elif i == "C":
             matchDNA += "G"

    return matchDNA

print(DNA_strand(dna))