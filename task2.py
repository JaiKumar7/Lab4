import string

def clean_book(fileName):
  ''' opens book and return list of cleaned words '''
  f1 = open(fileName)
  book = f1.read()
  tempBook = book.lower()
  cleanBook = ''
  for letter in tempBook:
    if letter not in string.punctuation:
      cleanBook += letter
  words = cleanBook.split()
  return words 

def count_words(words):
  print('Total words in book.txt are {}'.format(len(words)))

def freq(words):
  word_freq = {}
  for word in words:
    if word not in word_freq:
      word_freq[word] = words.count(word)
    else:
      pass
  sorted_word_freq = sorted(word_freq.items(), key = lambda kv: (kv[1],kv[0]), reverse= True)
  print('most freq 20 words are: ')
  for word, frq in sorted_word_freq[:20]:
    print('word -> "{}" frequency {}'.format(word, frq))

def count_diff_words(words):
  unq_words = []
  for word in words:
    if word not in unq_words:
      unq_words.append(word)
    else:
      pass
  print('{} number of different words are used in the book'.format(len(unq_words)))

words = clean_book('book.txt')
count_words(words)
freq(words)
count_diff_words(words)
