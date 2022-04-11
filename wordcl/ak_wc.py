import os
import string
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import spacy

txt = open(os.path.join('..', 'text', 'ak_orig_complete.txt'), 'r')
lines = txt.readlines()
txt.close()

clean_lines = []

for line in lines:
    if line.startswith('PART'):
        lines.remove(line)
    elif line.startswith('Chapter'):
        lines.remove(line)
    elif line.startswith('\n'):
        lines.remove(line)

for line in lines:
    clean_lines.append(line.strip())
# (messes up text if in first for loop)

clean_lines.pop(0)  # remove artifact in first position

clean_lines = [i.lower() for i in clean_lines]

clean_lines2 = []

for l in clean_lines:
    for letter in l:
        if letter in string.punctuation:
            l = l.replace(letter, '')
    clean_lines2.append(l)

clean_lines3 = []

clean_lines3 = ' '.join(clean_lines2).split(' ')

wc_str = ' '.join(clean_lines3)

wordcloud = WordCloud(width=2000, height=1000).generate(wc_str)
plt.figure(figsize=(20, 12))
plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('wordcl_1.png', bbox_inches='tight')
plt.show()
plt.close()

# problem: apostrophes separate words -> e.g. 's', 're', 't', see plot
# use stopwords.txt with stopwords parameter?

control_text = open(os.path.join('control_text.txt'), 'w')
control_text.write(wc_str)
control_text.close()

##########

nlp = spacy.load('en_core_web_trf', disable=['parser', 'ner'])  # keeping only tagger component needed for
# lemmatization


#  -> E088] Text of length 1865574 exceeds maximum of 1000000. The parser and NER models require roughly 1GB
# of temporary memory per 100,000 characters in the input. This means long texts may cause memory allocation errors.
# If you're not using the parser or NER, it's probably safe to increase the `nlp.max_length` limit.
# The limit is in number of characters, so you can check whether your inputs are too long by checking `len(text)

nlp.max_length = 2000000

# spacy.prefer_gpu()    # CUDA not working as of now

#####

test_str = "this is a string for testing purposes that shall be used to try lemmatizing some text."

#####

str2 = nlp(wc_str)
str3 = " ".join([token.lemma_ for token in str2])

# print(str3)

lem_txt = open(os.path.join('str3.txt'), 'w')
lem_txt.write(str3)
lem_txt.close()

# print(wc_str)
