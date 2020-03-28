from nltk import CFG
import nltk
from nltk.parse import RecursiveDescentParser
from nltk.parse import pchart
from nltk.parse import ShiftReduceParser

grammar = nltk.CFG.fromstring("""
S -> NP VP | VP
NP -> N | Det Nom | PropN | NP PP
Nom -> Adj Nom | N
VP -> V NP | V S | VP PP
PP -> P NP

PropN -> 'Bill' | 'Bob' | 'He'
Det -> 'the' | 'a' | 'an' | 'An' | 'The' | 'A' | 'on'| 'some' 
N -> 'bear' | 'squirrel' | 'park' | 'block' | 'table' | 'river' | 'dog' | 'dogs'| 'pasta' | 'anchovies' | 'restaurant' | 'fork' 
Adj -> 'angry' | 'frightened' | 'furry' 
V -> 'chased' | 'saw' | 'eats' | 'eat' | 'chase' | 'Put' | 'have' 
P -> 'on' | 'in' | 'along' | 'with' 

""")

##sentence1 = "He eats pasta with a fork in the restaurant".split()
##parser1 = nltk.ChartParser(grammar)
##for tree1 in parser1.parse(sentence1):
##    # print(tree1)
##     print (tree1.draw())

sr = ShiftReduceParser(grammar)
sentence1 = "He eats pasta with some anchovies in the restaurant"
tokens = nltk.word_tokenize(sentence1) 
for x in sr.parse(tokens):
     print(x.draw())

print ("-------------------------------------------------------------------")

sentence1 = "He eats pasta with some anchovies in the restaurant".split()
parser1 = nltk.EarleyChartParser(grammar, trace=2)

for tree1 in parser1.parse(sentence1):
    print(tree1)



