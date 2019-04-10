#walter sellars
#4140
#02/11/19
#c2e27.py
import nltk
from nltk.corpus import wordnet as wn

def convert(let): #takes the letter representing POS and returns its full name
    if let == 'n': return 'noun'
    elif let == 'v': return 'verb'
    elif let == 'r': return 'adverb'
    return 'adjective'

part= ['n', 'v', 'r', 'a']
pname = '' #name of part of speech for printing
words = list(wn.words())
seen_words = []
for p in part: #does each one
   pname = convert(p)
   counter = 0
   total = len(list(wn.all_synsets(p)))
   for x in words:
      counter += len(list(wn.synsets(x, p)))
   avg = round(counter/total, 2)
   print('Average polysemy for', pname, avg)
