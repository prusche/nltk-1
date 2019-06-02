#!usr/bin/python3

#chunking allows us to find groups of parts of speech together
#using RE to group them (i.e., prep+def art+noun)

import nltk
from nltk import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)

            #uses regular expressions
            chunkGram = r"""Chunk: {<RB.?>*<VB.?><NNP>+<NN>?} """

            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)

            #print(chunked)

            chunked.draw() #if Matplotlib

    except Exception as e:
        print(str(e))

process_content()
