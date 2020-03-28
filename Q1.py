from nltk import CFG
import nltk
from nltk.parse import RecursiveDescentParser
from nltk.parse import pchart

grammar = nltk.CFG.fromstring("""
S -> NP VP | VP 
NP -> N | Det Nom | PropN | NP PP
Nom -> Adj Nom | N
VP -> V NP | V S | VP PP
PP -> P NP
PropN -> 'Bill' | 'Bob' 
Det -> 'the' | 'a' | 'an' | 'An' | 'The' | 'A' | 'on'| 'some' 
N -> 'bear' | 'squirrel' | 'park' | 'block' | 'table' | 'river' | 'dog' | 'dogs'  
Adj -> 'angry' | 'frightened' | 'furry' 
V -> 'chased' | 'saw' | 'eats' | 'eat' | 'chase' | 'Put' | 'have' 
P -> 'on' | 'in' | 'along' 

""")

sentence1 = "Put the block on the table ".split()
parser1 = nltk.ChartParser(grammar)

for tree1 in parser1.parse(sentence1):
    print (tree1.draw())

print ("--------------------------------------------------------------------")

sentence2 = "Bob chased a bear in the park along the river".split()
parser2 = nltk.ChartParser(grammar)

for tree2 in parser2.parse(sentence2):
    print (tree2);
print ("--------------------------------------------------------------------")

sentence3 = "Bill saw Bob chase the angry furry dog".split()
parser3 = nltk.ChartParser(grammar)

for tree3 in parser3.parse(sentence3):
    print (tree3)
