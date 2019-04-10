import nltk
from nltk.corpus import brown

word_tags = nltk.bigrams(brown.tagged_words(tagset='universal'))
post_conj = [b[1] for (a, b) in word_tags if a[1] == 'CONJ']
post_no_conj = [b[1] for (a, b) in word_tags if a[1] != 'CONJ']

print("Parts of speech that never follow a conjunction:", [n for n in post_no_conj if n not in post_conj])
print("3 most common parts of speech that follow a conjunction that are not a noun or verb:", [tag for (tag,_)  in nltk.FreqDist(post_conj).most_common() if tag not in ['NOUN', 'VERB']][:3])
