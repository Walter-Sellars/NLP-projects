from nltk.corpus import brown
import nltk

brown_tag_words = brown.tagged_words()
cfd = nltk.ConditionalFreqDist(brown_tag_words)
conditions = cfd.conditions()

# creates a new array of word types that only have one distinct word tag
single_tag = [condition for condition in conditions if len(cfd[condition]) == 1]

#the proportion of tags that have only one POS tag.
prop_single_tag = len(single_tag) / len(conditions)
print(prop_single_tag)

#num ambiguous words.
number_single_tag = len(conditions) - len(single_tag)
print(number_single_tag)

#num of ambiguous word tokens in the total brown corpus
set_words = set(brown.words())
shared_words = [word for word in single_tag if word in set_words]
percen_brown = len(brown.words())/ len(shared_words)
print("percent of ambiguous words in brown corpus" + str(percen_brown))
