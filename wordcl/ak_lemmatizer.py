import os
import string
import spacy

non_lem_txt = open(os.path.join('control_text.txt'), 'r')
non_lem_txt.read()
non_lem_txt.close()

print(non_lem_txt)

nlp = spacy.load('en_core_web_trf', disable=['parser', 'ner'])
# keeping only tagger component needed for lemmatization


#  -> E088] Text of length 1865574 exceeds maximum of 1000000. The parser and NER models require roughly 1GB
# of temporary memory per 100,000 characters in the input. This means long texts may cause memory allocation errors.
# If you're not using the parser or NER, it's probably safe to increase the `nlp.max_length` limit.
# The limit is in number of characters, so you can check whether your inputs are too long by checking `len(text)

nlp.max_length = 2000000

# spacy.prefer_gpu()    / CUDA not working as of now

#####

test_str = "this is a string for testing purposes that shall be used to try lemmatizing some text."

#####

str2 = nlp(wc_str)

print(wc_str)

# print(str3)

lem_txt = open(os.path.join('str3.txt'), 'w')
lem_txt.write(str3)
lem_txt.close()

# print(wc_str)
