#!usr/bin/python3

#another way to separate out names

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

            #new code; binary=True will remove the categorization of the named entities, which can be wrong
            namedEnt = nltk.ne_chunk(tagged, binary=True)

            #namedEnt.draw() #if matplotlib
            print(namedEnt)

    except Exception as e:
        print(str(e))

process_content()
