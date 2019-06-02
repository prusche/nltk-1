#!/usr/bin/python3

#Tokenizing is splitting by sentences or words

from nltk.tokenize import sent_tokenize, word_tokenize

example_text = "Hello Mr. Smith, how are you doing today? The weather is great and Python is awesome. The sky is pinkish-blue. You should not eat cardboard."

#print each sentence of the text
print(sent_tokenize(example_text))

#print each word of the text -- notice that it catches Mr. as a word, and also punctuation
print(word_tokenize(example_text))

for i in word_tokenize(example_text):
    print(i)
