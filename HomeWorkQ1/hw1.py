import string

p = string.punctuation
w = string.whitespace

def open_file():
  try:
    f1 = open('wordList.txt')
    f2 = open('book.txt')
  except Exception as e:
    print(e)
  return f1, f2

def read_to_list(f1, f2): 
  bk = f2.read()
  wrds = f1.read()
  wordList = wrds.split()
  s = ''
  book = bk.lower()
  for char in book:
    if char not in p:
      s += char
    else:
      pass
  book_list = s.split()
  return wordList, book_list

def not_in_word_list(wordList, book_list):
  word_set = set(wordList)
  book_set = set(book_list)
  res_set = book_set.difference(word_set)
  return res_set

def common_words(book_list):
  d = {}
  common_wrd = []
  for i in book_list:
    if i not in d:
      d[i] = book_list.count(i)
    else:
      pass
  sd = sorted(d.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)
  for i, j in sd[:20]:
    common_wrd.append(i)
  return common_wrd

def cmnwrd_not_in_wrd_list(res_set, common_wrd, wordList):
  word_set = set(wordList)
  cmn = res_set.intersection(common_wrd)
  cmnNotInWordList = cmn.difference(word_set)
  return len(cmnNotInWordList)

f1, f2 = open_file()
wordList, book_list = read_to_list(f1, f2)
res_set = not_in_word_list(wordList, book_list)
print(' ***** words in book but not in word list *****')
print(res_set)
print()

common_wrd = common_words(book_list)
cmnNotInWordList = cmnwrd_not_in_wrd_list(res_set, common_wrd, wordList)
print('***** Common words of book which are not in word list *****')
print(cmnNotInWordList)