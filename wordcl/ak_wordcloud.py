import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# wordcloud for preprocessed text

with open(os.path.join('..', 'text', 'preprocessed', 'ak_complete_preprocessed.txt'), 'r', encoding='utf-8') as file:
    ak_complete = file.read()

with open(os.path.join('..', 'text', 'preprocessed', 'ak_p1_preprocessed.txt'), 'r', encoding='utf-8') as file:
    ak_p1 = file.read()

with open(os.path.join('..', 'text', 'preprocessed', 'ak_p2_preprocessed.txt'), 'r', encoding='utf-8') as file:
    ak_p2 = file.read()

with open(os.path.join('..', 'text', 'preprocessed', 'ak_p3_preprocessed.txt'), 'r', encoding='utf-8') as file:
    ak_p3 = file.read()

with open(os.path.join('..', 'text', 'preprocessed', 'ak_p4_preprocessed.txt'), 'r', encoding='utf-8') as file:
    ak_p4 = file.read()

with open(os.path.join('..', 'text', 'preprocessed', 'ak_p5_preprocessed.txt'), 'r', encoding='utf-8') as file:
    ak_p5 = file.read()

with open(os.path.join('..', 'text', 'preprocessed', 'ak_p6_preprocessed.txt'), 'r', encoding='utf-8') as file:
    ak_p6 = file.read()

with open(os.path.join('..', 'text', 'preprocessed', 'ak_p7_preprocessed.txt'), 'r', encoding='utf-8') as file:
    ak_p7 = file.read()

with open(os.path.join('..', 'text', 'preprocessed', 'ak_p8_preprocessed.txt'), 'r', encoding='utf-8') as file:
    ak_p8 = file.read()


# define function for wordcloud

def m_wordcloud(part, filename):
    # first: use stopwords list created in stopwords_extraction.py (todo: maybe remove this comment?)
    with open('stopwords.txt', 'r') as f:
        stopwords_pre = f.readlines()
        stopwords = []
        for e in stopwords_pre:
            stopwords.append(e.strip())
    wordcloud = WordCloud(width=2000, height=1000, stopwords=stopwords).generate(part)
    plt.figure(figsize=(20, 12))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.savefig(str(filename) + '.png', bbox_inches='tight')
    plt.show()
    plt.close()


# wordcloud for preprocessed texts

m_wordcloud(ak_complete, 'ak_complete')
m_wordcloud(ak_p1, 'ak_p1')
m_wordcloud(ak_p2, 'ak_p2')
m_wordcloud(ak_p3, 'ak_p3')
m_wordcloud(ak_p4, 'ak_p4')
m_wordcloud(ak_p5, 'ak_p5')
m_wordcloud(ak_p6, 'ak_p6')
m_wordcloud(ak_p7, 'ak_p7')
m_wordcloud(ak_p8, 'ak_p8')

# wordcloud for lemmatized text

with open(os.path.join('..', 'text', 'lemmatized', 'ak_complete_lem.txt'), 'r', encoding='utf-8') as file:
    ak_complete_lem = file.read()

with open(os.path.join('..', 'text', 'lemmatized', 'ak_p1_lem.txt'), 'r', encoding='utf-8') as file:
    ak_p1_lem = file.read()

with open(os.path.join('..', 'text', 'lemmatized', 'ak_p2_lem.txt'), 'r', encoding='utf-8') as file:
    ak_p2_lem = file.read()

with open(os.path.join('..', 'text', 'lemmatized', 'ak_p3_lem.txt'), 'r', encoding='utf-8') as file:
    ak_p3_lem = file.read()

with open(os.path.join('..', 'text', 'lemmatized', 'ak_p4_lem.txt'), 'r', encoding='utf-8') as file:
    ak_p4_lem = file.read()

with open(os.path.join('..', 'text', 'lemmatized', 'ak_p5_lem.txt'), 'r', encoding='utf-8') as file:
    ak_p5_lem = file.read()

with open(os.path.join('..', 'text', 'lemmatized', 'ak_p6_lem.txt'), 'r', encoding='utf-8') as file:
    ak_p6_lem = file.read()

with open(os.path.join('..', 'text', 'lemmatized', 'ak_p7_lem.txt'), 'r', encoding='utf-8') as file:
    ak_p7_lem = file.read()

with open(os.path.join('..', 'text', 'lemmatized', 'ak_p8_lem.txt'), 'r', encoding='utf-8') as file:
    ak_p8_lem = file.read()

m_wordcloud(ak_complete_lem, 'ak_complete_lem')
m_wordcloud(ak_p1_lem, 'ak_p1_lem')
m_wordcloud(ak_p2_lem, 'ak_p2_lem')
m_wordcloud(ak_p3_lem, 'ak_p3_lem')
m_wordcloud(ak_p4_lem, 'ak_p4_lem')
m_wordcloud(ak_p5_lem, 'ak_p5_lem')
m_wordcloud(ak_p6_lem, 'ak_p6_lem')
m_wordcloud(ak_p7_lem, 'ak_p7_lem')
m_wordcloud(ak_p8_lem, 'ak_p8_lem')
