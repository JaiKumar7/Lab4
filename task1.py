import string

space = string.whitespace
punctuations = string.punctuation
f1 = open('book.txt')
book = f1.readlines()
cleanBook = []
for line in book:
  cleanline = ""
  for char in line:
    if char not in punctuations and char not in space:
        cleanline = cleanline + char
  res = cleanline.lower()
  if len(res) > 0:
    cleanBook.append(res)
  else:
    pass
print(cleanBook)

