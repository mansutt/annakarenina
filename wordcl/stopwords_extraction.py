# code to extract stopwords from NLTK module for use in WordCloud module

from nltk.corpus import stopwords

with open('stopwords.txt', 'w') as file:
    for word in stopwords.words('english'):
        file.write(word + '\n')
