import sys
import operator
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def pathSimilarity(w1, w2):
    maxSim = 0
    synset1 = wn.synsets(w1)
    synset2 = wn.synsets(w2)
    for syn1 in synset1:
        for syn2 in synset2:
            sim = wn.path_similarity(syn1, syn2)
            if(sim is not None and sim > maxSim):
                maxSim = sim
    return maxSim

def hypernymPathSimilarity(w1, w2):
    maxSim = 0
    hh1 = ''
    hh2 = ''
    synset1 = wn.synsets(w1)
    synset2 = wn.synsets(w2)
    for syn1 in synset1:
        hyp1 = syn1.hypernyms()
        for syn2 in synset2:
            hyp2 = syn2.hypernyms()
            for h1 in hyp1:
                for h2 in hyp2:
                    sim = wn.path_similarity(h1, h2)
                    if(sim is not None and sim > maxSim):
                        maxSim = sim
                        hh1 = h1.name()
                        hh2 = h2.name()
    return hh1,hh2,maxSim

def goldSimilarity(w1, w2):
    goldStandard = open("GoldStandard.txt","r")
    sim = 0
    for line in goldStandard:
        word1, word2, s = line.split()
        if(word1 == w1 and word2 == w2):
            sim = s
            break
    goldStandard.close()
    return sim

def preProcess(text):
    #Punctuation
    puncChars = [".",",","?","!",";",":","-","'","\"","(",")","“","”","_","*","[","]"]
    for s in puncChars:
        text = text.replace(s," ")
   
    #Stopping
    stopWords = set(stopwords.words('english'))
    words = word_tokenize(text)
    wordsFiltered = []
    
    lemmatizer = WordNetLemmatizer() 
    
    for w in words:
        if w not in stopWords:
            wordsFiltered.append(lemmatizer.lemmatize(w))
    
    return list(set(wordsFiltered))

print("Q4. Calculating similarity between words")
fileName = input("Please enter the file name to process: ")
#fileName = "text1.txt"

try:
    file = open(fileName,"r",encoding="utf8")
    fileContents = file.readlines()
    fileContents = " ".join(fileContents)
except FileNotFoundError:
    sys.exit("File does not exist! Exiting...")

#Task 1   
simLex = open("SimLex999-100.txt","r")   
predicted = open("BioSim-100-predicted.txt", "w")

predicted.write("word1\tword2\tGoldSimilarity\tWordNetSimiliarity\n")    

next(simLex)
for line in simLex:
    w1,w2,s = line.split()
    sim = pathSimilarity(w1, w2)
    #gSim = goldSimilarity(w1, w2)
    predicted.write("{}\t{}\t{}\t{}\n".format(w1,w2,s,sim))  

#Task 2
tokens = preProcess(fileContents)
print (fileContents)
originalPairs = open("original-pairs.txt","w",encoding="utf8")
originalPairs.write("word1\tword2\tSimilarity\n")
for i,token1 in enumerate(tokens):
    for j,token2 in enumerate(tokens):
        if(i != j):
            originalPairs.write("{}\t{}\t{}\n".format(token1,token2,pathSimilarity(token1,token2)))

#Task 3          
originalPairsHypernyms = open("original-pairs-hypernyms.txt","w",encoding="utf8")
originalPairsHypernyms.write("word1\tword2\tSimilarity1\thyp1\thyp2\tSimilarity2")
for i,token1 in enumerate(tokens):
    for j,token2 in enumerate(tokens):
        if(i != j):
            hyp1, hyp2, hypSim = hypernymPathSimilarity(token1, token2)
            originalPairsHypernyms.write("{}\t{}\t{}\t{}\t{}\t{}\n".format(token1,token2,pathSimilarity(token1,token2),hyp1,hyp2,hypSim))

#Task 4
top = {}            
for i,token1 in enumerate(tokens):
    for j,token2 in enumerate(tokens):
        if(i != j):
            top[token1 + " " + token2] = pathSimilarity(token1,token2)

sortedTop = sorted(top.items(), key=operator.itemgetter(1), reverse=True)
top = open("top.txt","w")
for item in sortedTop[:10]:
    top.write("{}\t{}\n".format(item[0], item[1]))
            
simLex.close()
predicted.close()   
file.close()
originalPairs.close()
originalPairsHypernyms.close()
top.close()
