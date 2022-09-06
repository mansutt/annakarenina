import os
from matplotlib import pyplot as plt
from nltk.sentiment import SentimentIntensityAnalyzer

with open(os.path.join('../..', 'text', 'preprocessed', 'lemmatized', 'ak_complete_lem.txt'), 'r', encoding='utf-8') as file:
    ak_complete_lem = file.read()

with open(os.path.join('../..', 'text', 'preprocessed', 'lemmatized', 'ak_p1_lem.txt'), 'r', encoding='utf-8') as file:
    ak_p1_lem = file.read()

with open(os.path.join('../..', 'text', 'preprocessed', 'lemmatized', 'ak_p2_lem.txt'), 'r', encoding='utf-8') as file:
    ak_p2_lem = file.read()

with open(os.path.join('../..', 'text', 'preprocessed', 'lemmatized', 'ak_p3_lem.txt'), 'r', encoding='utf-8') as file:
    ak_p3_lem = file.read()

with open(os.path.join('../..', 'text', 'preprocessed', 'lemmatized', 'ak_p4_lem.txt'), 'r', encoding='utf-8') as file:
    ak_p4_lem = file.read()

with open(os.path.join('../..', 'text', 'preprocessed', 'lemmatized', 'ak_p5_lem.txt'), 'r', encoding='utf-8') as file:
    ak_p5_lem = file.read()

with open(os.path.join('../..', 'text', 'preprocessed', 'lemmatized', 'ak_p6_lem.txt'), 'r', encoding='utf-8') as file:
    ak_p6_lem = file.read()

with open(os.path.join('../..', 'text', 'preprocessed', 'lemmatized', 'ak_p7_lem.txt'), 'r', encoding='utf-8') as file:
    ak_p7_lem = file.read()

with open(os.path.join('../..', 'text', 'preprocessed', 'lemmatized', 'ak_p8_lem.txt'), 'r', encoding='utf-8') as file:
    ak_p8_lem = file.read()

sia = SentimentIntensityAnalyzer()

comp_sent = sia.polarity_scores(ak_complete_lem)
p1_sent = sia.polarity_scores(ak_p1_lem)
p2_sent = sia.polarity_scores(ak_p2_lem)
p3_sent = sia.polarity_scores(ak_p3_lem)
p4_sent = sia.polarity_scores(ak_p4_lem)
p5_sent = sia.polarity_scores(ak_p5_lem)
p6_sent = sia.polarity_scores(ak_p6_lem)
p7_sent = sia.polarity_scores(ak_p7_lem)
p8_sent = sia.polarity_scores(ak_p8_lem)

# exporting to diagram

def sent_barplot(input, filename, part):
    keys = input.keys()
    values = input.values()
    plt.bar(keys, values)
    plt.suptitle('Distribution of emotions in Part ' + str(part))
    plt.savefig(str(filename) + '.png', dpi=400)

sent_barplot(comp_sent, 'comp_sent', '1-8')
sent_barplot(p1_sent, 'p1_sent', 1)
sent_barplot(p2_sent, 'p2_sent', 2)
sent_barplot(p3_sent, 'p3_sent', 3)
sent_barplot(p4_sent, 'p4_sent', 4)
sent_barplot(p5_sent, 'p5_sent', 5)
sent_barplot(p6_sent, 'p6_sent', 6)
sent_barplot(p7_sent, 'p7_sent', 7)
sent_barplot(p8_sent, 'p8_sent', 8)

# todo: stacked barplot for each part in x-axis with emotion in y-axis
