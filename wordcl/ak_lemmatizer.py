import os
import spacy

nlp = spacy.load('en_core_web_trf', disable=['parser', 'ner'])
# keeping only tagger component needed for lemmatization

nlp.max_length = 2000000
# enhance max length of characters from 1 million to 2 million (Anna Karenina has about 1.8 million)

# read text parts

with open(os.path.join('..', 'text', 'preprocessed', 'ak_complete_preprocessed.txt'), 'r', encoding='utf-8') as file:
    ak_complete_non_lem = file.read()

with open(os.path.join('..', 'text', 'preprocessed', 'ak_p1_preprocessed.txt'), 'r', encoding='utf-8') as file:
    ak_p1_non_lem = file.read()

with open(os.path.join('..', 'text', 'preprocessed', 'ak_p2_preprocessed.txt'), 'r', encoding='utf-8') as file:
    ak_p2_non_lem = file.read()

with open(os.path.join('..', 'text', 'preprocessed', 'ak_p3_preprocessed.txt'), 'r', encoding='utf-8') as file:
    ak_p3_non_lem = file.read()

with open(os.path.join('..', 'text', 'preprocessed', 'ak_p4_preprocessed.txt'), 'r', encoding='utf-8') as file:
    ak_p4_non_lem = file.read()

with open(os.path.join('..', 'text', 'preprocessed', 'ak_p5_preprocessed.txt'), 'r', encoding='utf-8') as file:
    ak_p5_non_lem = file.read()

with open(os.path.join('..', 'text', 'preprocessed', 'ak_p6_preprocessed.txt'), 'r', encoding='utf-8') as file:
    ak_p6_non_lem = file.read()

with open(os.path.join('..', 'text', 'preprocessed', 'ak_p7_preprocessed.txt'), 'r', encoding='utf-8') as file:
    ak_p7_non_lem = file.read()

with open(os.path.join('..', 'text', 'preprocessed', 'ak_p8_preprocessed.txt'), 'r', encoding='utf-8') as file:
    ak_p8_non_lem = file.read()


def lemmatize(part, filename):
    pre_lem_txt = nlp(part)
    lem_txt = " ".join([token.lemma_ for token in pre_lem_txt])
    with open(os.path.join('..', 'text', 'lemmatized', str(filename) + '.txt'), 'w', encoding='utf-8') as output_file:
        output_file.write(lem_txt)


lemmatize(ak_complete_non_lem, 'ak_complete_lem')
lemmatize(ak_p1_non_lem, 'ak_p1_lem')
lemmatize(ak_p2_non_lem, 'ak_p2_lem')
lemmatize(ak_p3_non_lem, 'ak_p3_lem')
lemmatize(ak_p4_non_lem, 'ak_p4_lem')
lemmatize(ak_p5_non_lem, 'ak_p5_lem')
lemmatize(ak_p6_non_lem, 'ak_p6_lem')
lemmatize(ak_p7_non_lem, 'ak_p7_lem')
lemmatize(ak_p8_non_lem, 'ak_p8_lem')

# todo: another round of preprocessing to clean up text? + get rid of 's in preprocessed texts
