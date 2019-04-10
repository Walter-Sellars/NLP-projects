import nltk
from nltk.corpus import stopwords
from nltk.corpus import brown

bigramsWOstop = [(a,b) for a,b in nltk.bigrams(brown.words(categories="science_fiction")) if a not in stopwords.words('english') and b not in stopwords.words('english')]

bigramsWOstopfd = nltk.FreqDist(bigramsWOstop)

for line in bigramsWOstopfd.most_common(50):
	print(line)
