import nltk
from nltk.corpus import stopwords

swords = stopwords.words('english')
def bigrams(data):
	bi = nltk.bigrams(data)
	fd = nltk.FreqDist(bi)
	print(fd.most_common(50))

bigrams([w for w in text if w not in swords])
