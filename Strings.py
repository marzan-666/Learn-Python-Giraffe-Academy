print("Girffe\nAcademy")
phrase = "Learning site"
print(phrase + " is very cool") #concatenation

phrase = "abcd"
print(phrase.upper())
print(phrase.isupper())
phrase="ABCD"
print(phrase.isupper())
phrase = "efgh"
print(phrase.upper().isupper()) # made upper from lower and checked true or false

phrase = "my name is marzan"
print(phrase)
print(len(phrase))
phrase = "Marzan" #in python string counting/indexing starts from 0, so M is 0, a is 1 , r is 2 and so on. . .
print(phrase[0])
print(phrase[1])
print(phrase.index("M"))
print(phrase.index("a"))
phrase= "Md Marzan"
print(phrase.replace("Md","Mohammad"))