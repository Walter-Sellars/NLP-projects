import nltk
from nltk.corpus import brown

tagged_sents= brown.tagged_sents(categories='news')

#most common 100
fd = nltk.FreqDist(brown.words())
most_common = [tag for (tag,__) in fd.most_common(100)]

#modifies words not tags
def modify(corpus, f):
	new_corp = []
	for x in corpus:
		new_corp.append([(f(w, t), t) for (w, t) in x])
	return new_corp

#callable def to check if known or unkown
def unk(word, tag):
    if word in most_common:
        return word
    else:
        return 'UNK'

#i spent a flipping hour on this and I still can't figure out a way to one or two line it. Best I got was a double nested if condition in a loop, and that just seemed silly.
tagged_sents = modify(tagged_sents, unk)

#define demarcation of tagged sents to determine training set and testing set size
size = int(len(tagged_sents) * 0.9)
train = tagged_sents[:size]
test = tagged_sents[size:]

#null is untrained, tagger2 trains off of tagger1 and the default tagger
taggernull = nltk.BigramTagger(tagged_sents)
tagger0 = nltk.DefaultTagger('NN')
tagger1 = nltk.UnigramTagger(train, backoff=tagger0)
tagger2 = nltk.BigramTagger(train, backoff=tagger1)

print("untrained bigram % correct: %" + str(taggernull.evaluate(test)*100)[:5])
print("  trained bigram % correct: %" + str(tagger2.evaluate(test)*100)[:5])
print("\n             improvement of %" + str((tagger2.evaluate(test)*100)-(taggernull.evaluate(test)*100))[:5])

