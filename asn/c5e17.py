import nltk
from nltk.corpus import brown

cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
avgs = 0 
count = 0 
perf = [float(freq[freq.max()])/freq.N() for (x, freq) in cfd.items()]
print(sum(perf)/len(perf))
