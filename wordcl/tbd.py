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