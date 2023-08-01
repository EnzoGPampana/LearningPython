# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
name = "Enzo Garofalo"

names = name.split()
initials = ""

for i in names:

    initials += i[0].upper() + "."

print(initials)    
