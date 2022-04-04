import numpy as np
import pandas as pd
import os
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import string
# string.punctuation

import matplotlib.pyplot as plt

import re

df = open(os.path.join('..', 'text', 'ak_pure_complete.txt'), "r")
lines = df.readlines()
df.close()

# remove /n at the end of each line
for index, line in enumerate(lines):
    lines[index] = line.strip()



#creating a dataframe(consider u want to convert your data to 2 columns)

df_result = pd.DataFrame(columns=('first_col', 'second_col'))
i = 0
first_col = ""
second_col = ""
for line in lines:
    # you can use "if" and "replace" in case you had some conditions to manipulate the txt data
    if 'X' in line:
        first_col = line.replace('X', "")
    else:
        # you have to kind of define what are the values in columns,for example second column includes:
        second_col = re.sub(r' \(.*', "", line)
        # this is how you create next line data
        df_result.loc[i] = [first_col, second_col]
        i = i+1





# ak = pd.read_csv(os.path.join('..', 'text', 'ak_pure_complete.txt'),
#                  index_col=0, sep=' ', header=None)

# print(ak)
# expanding the dispay of text sms column
# pd.set_option('display.max_colwidth', -1)
# print(ak.head())

# def remove_punctuation(text):
 #    punctuationfree="".join([i for i in text if i not in string.punctuation])
 #    return punctuationfree
# storing the puntuation free text
# ak['punctfree']= ak['v2'].apply(lambda x:remove_punctuation(x))
