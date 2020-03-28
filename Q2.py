from nltk import CFG
import nltk
from nltk.parse import RecursiveDescentParser
from nltk.parse import pchart
from nltk.parse import ShiftReduceParser

grammar = nltk.CFG.fromstring("""
S -> NP VP | VP PP | VP
NP -> Det Nom | PropN | NP PP| Det Nom PP |NNP
Nom -> Adj Nom | N
VP -> V NP | V S | V PP |  VP N PP | VB | VB NP | VB NP NP | VB NP  PP | VB S |  VP Adj
PP -> P NP | P S
PropN -> 'Bill' | 'Bob' 
Det -> 'the' | 'a' | 'an' | 'An' | 'The' | 'A' | 'on'| 'some' 
N -> 'bear' | 'squirrel' | 'park' | 'block' | 'table' | 'river' | 'dog' | 'dogs'  
Adj -> 'angry' | 'frightened' | 'furry' 
V -> 'chased' | 'saw' | 'eats' | 'eat' | 'chase' | 'Put' | 'have' 
P -> 'on' | 'in' | 'along' 
""")


## With the chartParser 
sentence1 = 'An bear eats an squirrel'.split()
parser1 = nltk.ChartParser(grammar)

for tree1 in parser1.parse(sentence1):
    print (tree1.draw())
    
## With the shiftReduceParser
sr = ShiftReduceParser(grammar)
sentence1 = 'An bear eats an squirrel'
tokens = nltk.word_tokenize(sentence1) 
for x in sr.parse(tokens):
     print(x)



