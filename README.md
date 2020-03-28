# Parsing And Word Similarity 

Instruction to run the code: 
Step1 - Open CMD and navigate to the folder containing the files (or Shift, right click, open power shell window here)
step 2 - there are 4 files for Q4 so to run a desired one type either "python Q4.Task1.py" or "python Q4.Task2.py" or "python Q4.Task3.py" or "python Q4.Task3.py" (if does not work, try without "python")
The program only runs on Python 3.7 and not on Python 2.7

Q1 to Q3 is is discussed in the report provided. 

Q4

A program was build to calculate word similarity in BioSim-100.txt using WordNet. For each
word pair in BioSim-100.txt you will calculate the WordNet similarity between the pair, using the
path similarity function implemented in NLTK, and print this into a file, along with the gold standard
similarity.

A program was build to detect word similarity in other texts. You will need to pre-process the user
specified input text, reading the file, performing sentence splitting, tokenization and lemmatization, and removing stopwords and punctuation. The resulting file should contain only content words, one word
per line. For each word in the file you will calculate the WordNet path similarity between the pair, and
print this into a file. Now apply your program to the file text1.txt.

Each word was replaced by hypernym and calculate the similarities between each word pair printing
this additional information to the file original-pairs-hypernyms.txt
