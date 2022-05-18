import os
from nltk.sentiment import SentimentIntensityAnalyzer

with open(os.path.join('..', 'text', 'lemmatized', 'ak_p1_lem.txt'), 'r', encoding='utf-8') as file:
    p1 = file.read()

with open(os.path.join('..', 'text', 'lemmatized', 'str3.txt'), 'r', encoding='utf-8') as file:
    comp = file.read()

sia = SentimentIntensityAnalyzer()
print(sia.polarity_scores(p1))
print(sia.polarity_scores(comp))
