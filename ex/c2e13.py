import nltk

from nltk.corpus import wordnet as wn

no_hyp_nouns=[noun for noun in wn.all_synsets('n') if len(noun.hyponyms())==0]

all_noun_words=[noun for noun in wn.all_synsets('n')]

print("Percentage of noun having no hyponyms: ",len(no_hyp_nouns)/len(all_noun_words)*100)

