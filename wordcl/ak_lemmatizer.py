import os
import spacy

with open(os.path.join('control_text.txt'), 'r', encoding='utf-8') as file:
    non_lem_txt = file.read()

nlp = spacy.load('en_core_web_trf', disable=['parser', 'ner'])
# keeping only tagger component needed for lemmatization

nlp.max_length = 2000000
# enhance max length of characters from 1 mil to 2 mil (AK has about 1.8 mil)

pre_lem_txt = nlp(non_lem_txt)
lem_txt = " ".join([token.lemma_ for token in pre_lem_txt])

with open(os.path.join('ak_lem.txt'), 'w', encoding='utf-8') as output_file:
    output_file.write(lem_txt)
