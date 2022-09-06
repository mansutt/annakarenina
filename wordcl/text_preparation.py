import os
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def preprocessing(input_text):
    clean_lines = []
    for line in input_text:
        if line.startswith('PART'):
            input_text.remove(line)
        elif line.startswith('Chapter'):
            input_text.remove(line)
        elif line.startswith('\n'):
            input_text.remove(line)
    for line in input_text:                 # (messes up text if in first for loop)
        clean_lines.append(line.strip())
    clean_lines2 = []
    for li in clean_lines:
        for letter in li:
            if letter in string.punctuation:
                li = li.replace(letter, '')
        clean_lines2.append(li)
    clean_lines3 = []
    clean_lines3 = ' '.join(clean_lines2).split(' ')
    wc_str = ' '.join(clean_lines3)
    return wc_str

# todo: change name of wc_str (only preprocessing, not directly related to wordcloud)


#####

# open all text parts
with open(os.path.join('..', 'text', 'parts', 'ak_complete.txt'), 'r', encoding='utf-8') as file:
    ak_complete = file.readlines()

with open(os.path.join('..', 'text', 'parts', 'ak_p1.txt'), 'r', encoding='utf-8') as file:
    ak_p1 = file.readlines()

with open(os.path.join('..', 'text', 'parts', 'ak_p2.txt'), 'r', encoding='utf-8') as file:
    ak_p2 = file.readlines()
    ak_p2.pop(0)
    ak_p2.pop(0)  # todo: clean this up (necessary to cut out "chapter" -> why though?)

with open(os.path.join('..', 'text', 'parts', 'ak_p3.txt'), 'r', encoding='utf-8') as file:
    ak_p3 = file.readlines()

with open(os.path.join('..', 'text', 'parts', 'ak_p4.txt'), 'r', encoding='utf-8') as file:
    ak_p4 = file.readlines()

with open(os.path.join('..', 'text', 'parts', 'ak_p5.txt'), 'r', encoding='utf-8') as file:
    ak_p5 = file.readlines()
    ak_p5.pop(0)
    ak_p5.pop(0)  # clean this up (necessary to cut out "PART" & "chapter" -> why though?)

with open(os.path.join('..', 'text', 'parts', 'ak_p6.txt'), 'r', encoding='utf-8') as file:
    ak_p6 = file.readlines()

with open(os.path.join('..', 'text', 'parts', 'ak_p7.txt'), 'r', encoding='utf-8') as file:
    ak_p7 = file.readlines()

with open(os.path.join('..', 'text', 'parts', 'ak_p8.txt'), 'r', encoding='utf-8') as file:
    ak_p8 = file.readlines()

# perform preprocessing on all text parts
clean_text_complete = preprocessing(ak_complete)
clean_text_p1 = preprocessing(ak_p1)
clean_text_p2 = preprocessing(ak_p2)
clean_text_p3 = preprocessing(ak_p3)
clean_text_p4 = preprocessing(ak_p4)
clean_text_p5 = preprocessing(ak_p5)
clean_text_p6 = preprocessing(ak_p6)
clean_text_p7 = preprocessing(ak_p7)
clean_text_p8 = preprocessing(ak_p8)

# save the preprocessed texts to text files
# todo: build save into function

with open(os.path.join('..', 'text', 'preprocessed', 'ak_complete_preprocessed.txt'), 'w', encoding='utf-8') as file:
    file.write(clean_text_complete)

with open(os.path.join('..', 'text', 'preprocessed', 'ak_p1_preprocessed.txt'), 'w', encoding='utf-8') as file:
    file.write(clean_text_p1)

with open(os.path.join('..', 'text', 'preprocessed', 'ak_p2_preprocessed.txt'), 'w', encoding='utf-8') as file:
    file.write(clean_text_p2)

with open(os.path.join('..', 'text', 'preprocessed', 'ak_p3_preprocessed.txt'), 'w', encoding='utf-8') as file:
    file.write(clean_text_p3)

with open(os.path.join('..', 'text', 'preprocessed', 'ak_p4_preprocessed.txt'), 'w', encoding='utf-8') as file:
    file.write(clean_text_p4)

with open(os.path.join('..', 'text', 'preprocessed', 'ak_p5_preprocessed.txt'), 'w', encoding='utf-8') as file:
    file.write(clean_text_p5)

with open(os.path.join('..', 'text', 'preprocessed', 'ak_p6_preprocessed.txt'), 'w', encoding='utf-8') as file:
    file.write(clean_text_p6)

with open(os.path.join('..', 'text', 'preprocessed', 'ak_p7_preprocessed.txt'), 'w', encoding='utf-8') as file:
    file.write(clean_text_p7)

with open(os.path.join('..', 'text', 'preprocessed', 'ak_p8_preprocessed.txt'), 'w', encoding='utf-8') as file:
    file.write(clean_text_p8)

# preprocessing on lemmatized texts

with open(os.path.join('..', 'text', 'lemmatized', 'ak_complete_lem.txt'), 'r', encoding='utf-8') as file:
    ak_complete_pp_lem = file.readlines()

with open(os.path.join('..', 'text', 'lemmatized', 'ak_p1_lem.txt'), 'r', encoding='utf-8') as file:
    ak_p1_pp_lem = file.readlines()

with open(os.path.join('..', 'text', 'lemmatized', 'ak_p2_lem.txt'), 'r', encoding='utf-8') as file:
    ak_p2_pp_lem = file.readlines()

with open(os.path.join('..', 'text', 'lemmatized', 'ak_p3_lem.txt'), 'r', encoding='utf-8') as file:
    ak_p3_pp_lem = file.readlines()

with open(os.path.join('..', 'text', 'lemmatized', 'ak_p4_lem.txt'), 'r', encoding='utf-8') as file:
    ak_p4_pp_lem = file.readlines()

with open(os.path.join('..', 'text', 'lemmatized', 'ak_p5_lem.txt'), 'r', encoding='utf-8') as file:
    ak_p5_pp_lem = file.readlines()

with open(os.path.join('..', 'text', 'lemmatized', 'ak_p6_lem.txt'), 'r', encoding='utf-8') as file:
    ak_p6_pp_lem = file.readlines()

with open(os.path.join('..', 'text', 'lemmatized', 'ak_p7_lem.txt'), 'r', encoding='utf-8') as file:
    ak_p7_pp_lem = file.readlines()

with open(os.path.join('..', 'text', 'lemmatized', 'ak_p8_lem.txt'), 'r', encoding='utf-8') as file:
    ak_p8_pp_lem = file.readlines()

ak_complete_prp_lem = preprocessing(ak_complete_pp_lem)
ak_p1_prp_lem = preprocessing(ak_p1_pp_lem)
ak_p2_prp_lem = preprocessing(ak_p2_pp_lem)
ak_p3_prp_lem = preprocessing(ak_p3_pp_lem)
ak_p4_prp_lem = preprocessing(ak_p4_pp_lem)
ak_p5_prp_lem = preprocessing(ak_p5_pp_lem)
ak_p6_prp_lem = preprocessing(ak_p6_pp_lem)
ak_p7_prp_lem = preprocessing(ak_p7_pp_lem)
ak_p8_prp_lem = preprocessing(ak_p8_pp_lem)

with open(os.path.join('..', 'text', 'preprocessed', 'lemmatized', 'ak_complete_prp_lem.txt'), 'w',
          encoding='utf-8') as file:
    file.write(ak_complete_prp_lem)

with open(os.path.join('..', 'text', 'preprocessed', 'lemmatized', 'ak_p1_prp_lem.txt'), 'w', encoding='utf-8') as file:
    file.write(ak_p1_prp_lem)

with open(os.path.join('..', 'text', 'preprocessed', 'lemmatized', 'ak_p2_prp_lem.txt'), 'w', encoding='utf-8') as file:
    file.write(ak_p2_prp_lem)

with open(os.path.join('..', 'text', 'preprocessed', 'lemmatized', 'ak_p3_prp_lem.txt'), 'w', encoding='utf-8') as file:
    file.write(ak_p3_prp_lem)

with open(os.path.join('..', 'text', 'preprocessed', 'lemmatized', 'ak_p4_prp_lem.txt'), 'w', encoding='utf-8') as file:
    file.write(ak_p4_prp_lem)

with open(os.path.join('..', 'text', 'preprocessed', 'lemmatized', 'ak_p5_prp_lem.txt'), 'w', encoding='utf-8') as file:
    file.write(ak_p5_prp_lem)

with open(os.path.join('..', 'text', 'preprocessed', 'lemmatized', 'ak_p6_prp_lem.txt'), 'w', encoding='utf-8') as file:
    file.write(ak_p6_prp_lem)

with open(os.path.join('..', 'text', 'preprocessed', 'lemmatized', 'ak_p7_prp_lem.txt'), 'w', encoding='utf-8') as file:
    file.write(ak_p7_prp_lem)

with open(os.path.join('..', 'text', 'preprocessed', 'lemmatized', 'ak_p8_prp_lem.txt'), 'w', encoding='utf-8') as file:
    file.write(ak_p8_prp_lem)

###

# directory = os.path.join('..', 'text', 'parts')
# for filename in os.listdir(directory):
#     f = os.path.join(directory, filename)
#     if os.path.isfile(f):
#         with open(filename, 'r', encoding='utf-8') as fn:
#             filename = filename
#
#
# maybe: iterate over dedicated folder with each part of the book

# todo: implement stopwords for 'S and other artifacts
