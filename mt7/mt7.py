# Midterm question 7 Program Template
# Walter Sellars
# mt7.py
# command line form python3 mt7.py <document> <numSentences> <maxLength>
# <document> is the prefix of the Gutenberg book
# <numSentences> is the number of sentences to be printed
# <maxLength> is the maximum word length of a printable sentence

# Required imports
import nltk
import re,sys
from nltk.corpus import gutenberg
from operator import itemgetter

#--------------------------------------------------------------------------
# summarize(document,numSent,maxLength) calculates the numSent highest scoring
# sentences whose word length does not exceed maxLength and prints them out
# in the order they appear in document
# scoring is sum of word frequencies

def summarize(document,numSent,maxLength):

#  Use appropriate specification of nltk.Text to generate the words for
#  calculating the frequency distribution.  DO NOT normalize for case
    corpus_freq = nltk.FreqDist([w for w in nltk.corpus.gutenberg.words(document) if w.isalnum()])
  
#  Use appropriate specification of nltk.sent_tokenize to generate the list
#  of sentences in the document.
    sent_corpus = nltk.corpus.gutenberg.sents(document)

#  Use appropriate regular expression functionality to generate a parallel
#  list of the sentences in the document broken down into the actual words
#  (eliminating special characters)
#  NOTE: for our purpose words consist of 1 or more alphanumeric characters
#  NOTE: DO NOT normalize for case
    sent_parallel_list = [[w for w in l if w.isalnum()] for l in sent_corpus]

#  Code to finish the processing goes here.  The form of the sentence to
#  be printed should be the form produced by breaking down the original list
#  into actual words
    score = [(i, sum([corpus_freq[word] for word in sent])) for i,sent in enumerate(sent_parallel_list) if len(sent) <= maxLength]
    score_sort = sorted(sorted(score, key=lambda x: x[1], reverse=True)[:numSent], key=lambda x: x[0])
    #sentData = sorted([(sum([corpus_freq[w] for w in k]),k) for k in sent_parallel_list if len(k) <= maxLength]).reverse()
    #print_list = [(corpus_freq, ' '.join(sent)) for (corpus_freq, sent) in score_sort]
    print_set = [" ".join(w for w in sent_parallel_list[i]) for (i,_) in score_sort]
    print(print_set)
    return
# summarize definition ends here
#--------------------------------------------------------------------------
# initial processing: grabs the command line arguments and calls summarize

docname = sys.argv[1]
numsentences = int(sys.argv[2])
maxL = int(sys.argv[3])
summarize (docname+".txt",numsentences,maxL)
