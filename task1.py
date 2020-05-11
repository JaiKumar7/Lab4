import string

space = string.whitespace
punctuations = string.punctuation
f1 = open('book.txt')
book = f1.read()
b1 = book.lower()
cleanBook = ""
for char in b1:
   if char not in punctuations and char not in space:
       cleanBook = cleanBook + char

print(cleanBook)

