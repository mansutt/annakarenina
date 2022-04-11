import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt

with open(os.path.join('str3.txt'), 'r', encoding='utf-8') as file:
    lem_txt = file.read()

lem_wordcloud = WordCloud(width=2000, height=1000).generate(lem_txt)
plt.figure(figsize=(20, 12))
plt.imshow(lem_wordcloud)
plt.axis('off')
plt.savefig('wordcl_lem.png', bbox_inches='tight')
plt.show()
plt.close()
