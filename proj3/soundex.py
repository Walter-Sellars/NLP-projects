# Walter Sellars
# soundex.py template
# CSCI 4140

# input - python3 soundex.py <test.txt>
# where test.tx is a file containing last names seperated by a newline

import sys
import nltk
import re


# Define tuple list and mapping code to create dictionary for consonant
# transformations at this point
mapping = [('[.,?!]', ''),('[bfpv]', '1'),('[cgjkqsxz]', '2'), ('[dt]', '3'), ('[l]', '4'), ('[mn]', '5'), ('[r]', '6')]
vowels = [('aeiouy', '')]


# function that takes token, transforms it into its new form, and returns it

def wordmap(token) :
    stringtoken = token.lower() #lowercase
    first = stringtoken[0] #tokenize
    stringtoken = first + re.sub('[wh]', '', stringtoken[1:])#remove non-first w and h
  
    #substitute consonants
    for (x,y) in mapping:
      stringtoken = re.sub(x, y, stringtoken)

    #replace adjacents
    stringtoken = list(stringtoken)
    for i in range(1, len(stringtoken)):
      if stringtoken[i] == stringtoken[i-1]:
        stringtoken[i] = ''
    stringtoken = ''.join(stringtoken)

    #remove vowels besides first
    stringtoken = first + re.sub('[aeiouy]', '', stringtoken[1:])

    #replace 1st symbol if digit
    if(stringtoken[0].isdigit()):
      stringtoken = first + stringtoken[1:]
    
    #append zeroes if there are less than 3 digits. Cut off excess digits after 3.
    while (len(stringtoken)<= 4):
      stringtoken = stringtoken + '0'

    stringtoken = stringtoken[:4]
    return stringtoken
    
    
    

# Driver code for the program
# sys.argv[1] should be the name of the input file
# sys.argv[0] will be the name of this file

for line in open(sys.argv[1]).readlines():
  text = nltk.word_tokenize(line.lower())
  for token in text:
    print (wordmap(token),end=' ')
  print()  # This prints new line at the end of processing a line


