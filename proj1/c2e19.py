#Walter Sellars
#c2e19
#1/30/19
#csci4140
# Write a program to create a table of word frequencies by genre, like the one given in 1 for modals. Choose your own words and try to find words whose presence (or absence) is typical of a genre. Discuss your findings.


import nltk
from nltk.corpus import brown

#genres to check - editable
genres = ["government", "religion", "lore", "news", "humor"]

cfd = nltk.ConditionalFreqDist((genre,word)for genre in genres for word in brown.words(categories=genre))

# check distribution of words - editable
words = ["life", "freedom", "love", "money", "growth", "happy", "work", "poor", "children",]

#conditional frequency distributions words by genres
cfd.tabulate(conditions=genres, samples=words)
