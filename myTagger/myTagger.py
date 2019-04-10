#Walter Sellars
#Assignment 4 - myTagger.py
#Due: 4/05/19
#CSCI 4140 - Natural Language Processing


import nltk
from nltk.corpus import brown as br
from random import shuffle

#number of folds for n-fold cross validation
folds = 10

sources = br.fileids()
sents = [s for f in sources for s in br.tagged_sents(f)]

#comment out for non-random
shuffle(sources)
shuffle(sents)


def tagFileID(data, folds):
    
    results = []
    foldNum = len(sources)//folds
    print("Results by Source nonrandom data  \n##################################")
    print("{:>13}".format("Test Fold") + "{:>14}".format("Result"))
    for i in range(0,10):
        low, high = i*foldNum, (i+1)*foldNum
        if i == 0: train = br.tagged_sents(data[high:]); test = br.tagged_sents(data[:high]) #assign sets for traiing and test - 3 cases: 1&2, first and last fold are test, 3 is all other cases
        elif i == folds-1: train = br.tagged_sents(data[:low]); test = br.tagged_sents(data[low:])
        else: train = br.tagged_sents(data[:low]) + br.tagged_sents(data[high:]); test = br.tagged_sents(data[low:high])

            
        #tagger evaluation
        t0 = nltk.DefaultTagger('NN')
        t1 = nltk.UnigramTagger(train, backoff=t0)
        t2 = nltk.BigramTagger(train, backoff=t1)

        #store eval results
        results.append(t2.evaluate(test))
        print("{:>9}".format(i+1) + "{:>17.1%}".format(results[i]))
    
    print("")
    return(results)

#trains and evaluates tagger given a folded dataset using ML cross-validation principles
def tag(data, folds):

    #print table header
    print("Results by Sentence nonrandom data\n##################################")
    print("{:>13}".format("Test Fold") + "{:>14}".format("Result"))

    results = []#holds results
    size = len(data) #total indexes of passed dataset 
    foldNum = size//folds #number of indexes in each fold
    count = 0#counter for output
    for i in range(0,size,foldNum):
        low, high = int(i), int(i+foldNum) #sets bracket of training datasets
        if i == 0: train = data[high:]; test = data[:high] #assign sets for traiing and test - 3 cases: 1&2, first and last fold are test, 3 is all other cases
        elif i == size-foldNum: train = data[:low]; test = data[low:]
        else: train = data[:low] + data[high:]; test = data[low:high]
        
        #tagger evaluation
        t0 = nltk.DefaultTagger('NN')
        t1 = nltk.UnigramTagger(train, backoff=t0)
        t2 = nltk.BigramTagger(train, backoff=t1)

        #store eval results
        results.append(t2.evaluate(test))
        print("{:>9}".format(count) + "{:>17.1%}".format(results[count]))
        count +=1

    print("")
    return(results)


fileIdRes = tagFileID(sources, folds)
sentRes = tag(sents, folds)
