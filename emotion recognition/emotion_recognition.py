# This code was inspired by the article "Emotion Recognition using Text" by Abhinav Kumar

# todo: clean up imports (sort alphabetically? remove unused)
# todo: change file locations from GDrive to local

import pandas as pd
import numpy as np
import re
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from keras.models import load_model
import urllib.request
import zipfile
import os
from keras.models import Sequential
from keras.layers import Embedding, Bidirectional, LSTM, GRU, Dense
import nltk
import nltk.data
from nltk.tokenize import word_tokenize
import warnings
import tensorflow as tf

nltk.download('punkt')
warnings.filterwarnings('ignore')

f = open('/content/drive/MyDrive/train.txt', 'r')
x_train = []
y_train = []
for i in f:
    l = i.split(';')
    y_train.append(l[1].strip())
    x_train.append(l[0])
f = open('/content/drive/MyDrive/test.txt', 'r')
x_test = []
y_test = []
for i in f:
    l = i.split(';')
    y_test.append(l[1].strip())
    x_test.append(l[0])
f = open('/content/drive/MyDrive/val.txt', 'r')
for i in f:
    l = i.split(';')
    y_test.append(l[1].strip())
    x_test.append(l[0])
data_train = pd.DataFrame({'Text': x_train, 'Emotion': y_train})
data_test = pd.DataFrame({'Text': x_test, 'Emotion': y_test})
data = data_train.append(data_test, ignore_index=True)


def clean_text(data):
    data = re.sub(r"(#[\d\w\.]+)", '', data)
    data = re.sub(r"(@[\d\w\.]+)", '', data)
    data = word_tokenize(data)
    return data


texts = [' '.join(clean_text(text)) for text in data.Text]
texts_train = [' '.join(clean_text(text)) for text in x_train]
texts_test = [' '.join(clean_text(text)) for text in x_test]

tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)
sequence_train = tokenizer.texts_to_sequences(texts_train)
sequence_test = tokenizer.texts_to_sequences(texts_test)
index_of_words = tokenizer.word_index
vocab_size = len(index_of_words) + 1

num_classes = 6
embed_num_dims = 300
max_seq_len = 500
class_names = ['anger', 'sadness', 'fear', 'joy', 'surprise', 'love']

X_train_pad = pad_sequences(sequence_train, maxlen=max_seq_len)
X_test_pad = pad_sequences(sequence_test, maxlen=max_seq_len)

encoding = {'anger': 0, 'sadness': 1, 'fear': 2, 'joy': 3, 'surprise': 4, 'love': 5}
y_train = [encoding[x] for x in data_train.Emotion]
y_test = [encoding[x] for x in data_test.Emotion]
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)


def create_embedding_matrix(filepath, word_index, embedding_dim):
    vocab_size = len(word_index) + 1
    embedding_matrix = np.zeros((vocab_size, embedding_dim))
    with open(filepath) as f:
        for line in f:
            word, *vector = line.split()
            if word in word_index:
                idx = word_index[word]
                embedding_matrix[idx] = np.array(vector, dtype=np.float32)[:embedding_dim]
    return embedding_matrix


fname = 'drive/MyDrive/embeddings/wiki-news-300d-1M.vec'
embedd_matrix = create_embedding_matrix(fname, index_of_words, embed_num_dims)

# add embedding, bidirectional and dense layer

embedd_layer = Embedding(vocab_size, embed_num_dims, input_length=max_seq_len, weights=[embedd_matrix], trainable=False)
gru_output_size = 128
bidirectional = True
model = Sequential()
model.add(embedd_layer)
model.add(Bidirectional(GRU(units=gru_output_size, dropout=0.2, recurrent_dropout=0.2)))
model.add(Dense(num_classes, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

batch_size = 128
epochs = 8
hist = model.fit(X_train_pad, y_train, batch_size=batch_size, epochs=epochs, validation_data=(X_test_pad, y_test))

tf.keras.models.save_model(model, 'textmodel', overwrite=True, include_optimizer=True,
                           save_format=None, signatures=None, options=None)


def preprocessing(input_text):
    clean_lines = []
    for line in input_text:
        if line.startswith('PART'):
            input_text.remove(line)
        elif line.startswith('Chapter'):
            input_text.remove(line)
        elif line.startswith('\n'):
            input_text.remove(line)
    for line in input_text:  # (messes up text if in first for loop)
        clean_lines.append(line.strip())
    clean_lines2 = ' '.join(clean_lines).split(' ')
    wc_str = ' '.join(clean_lines2)
    return wc_str



with open(('/content/drive/MyDrive/ak_p1.txt'), 'r', encoding='utf-8') as f:
    ak_p1 = f.readlines()
with open(('/content/drive/MyDrive/ak_p2.txt'), 'r', encoding='utf-8') as f:
    ak_p2 = f.readlines()
with open(('/content/drive/MyDrive/ak_p3.txt'), 'r', encoding='utf-8') as f:
    ak_p3 = f.readlines()
with open(('/content/drive/MyDrive/ak_p4.txt'), 'r', encoding='utf-8') as f:
    ak_p4 = f.readlines()
with open(('/content/drive/MyDrive/ak_p5.txt'), 'r', encoding='utf-8') as f:
    ak_p5 = f.readlines()
with open(('/content/drive/MyDrive/ak_p6.txt'), 'r', encoding='utf-8') as f:
    ak_p6 = f.readlines()
with open(('/content/drive/MyDrive/ak_p7.txt'), 'r', encoding='utf-8') as f:
    ak_p7 = f.readlines()
with open(('/content/drive/MyDrive/ak_p8.txt'), 'r', encoding='utf-8') as f:
    ak_p8 = f.readlines()

ak_p1n = preprocessing(ak_p1)
ak_p2n = preprocessing(ak_p2)
ak_p3n = preprocessing(ak_p3)
ak_p4n = preprocessing(ak_p4)
ak_p5n = preprocessing(ak_p5)
ak_p6n = preprocessing(ak_p6)
ak_p7n = preprocessing(ak_p7)
ak_p8n = preprocessing(ak_p8)

import nltk.data

nltk_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

sentences = []
sentences2 = []
sentences3 = []
sentences4 = []
sentences5 = []
sentences6 = []
sentences7 = []
sentences8 = []

for sentence in nltk_tokenizer.tokenize(ak_p1n.strip()):
    sentences.append(sentence)

for sentence in nltk_tokenizer.tokenize(ak_p2n.strip()):
    sentences2.append(sentence)

for sentence in nltk_tokenizer.tokenize(ak_p3n.strip()):
    sentences3.append(sentence)

for sentence in nltk_tokenizer.tokenize(ak_p4n.strip()):
    sentences4.append(sentence)

for sentence in nltk_tokenizer.tokenize(ak_p5n.strip()):
    sentences5.append(sentence)

for sentence in nltk_tokenizer.tokenize(ak_p6n.strip()):
    sentences6.append(sentence)

for sentence in nltk_tokenizer.tokenize(ak_p7n.strip()):
    sentences7.append(sentence)

for sentence in nltk_tokenizer.tokenize(ak_p8n.strip()):
    sentences8.append(sentence)

df = pd.DataFrame(sentences)
df2 = pd.DataFrame(sentences2)
df3 = pd.DataFrame(sentences3)
df4 = pd.DataFrame(sentences4)
df5 = pd.DataFrame(sentences5)
df6 = pd.DataFrame(sentences6)
df7 = pd.DataFrame(sentences7)
df8 = pd.DataFrame(sentences8)


def lists_in_list(lst):
    return [[e] for e in lst]


sentences = lists_in_list(sentences)
sentences2 = lists_in_list(sentences2)
sentences3 = lists_in_list(sentences3)
sentences4 = lists_in_list(sentences4)
sentences5 = lists_in_list(sentences5)
sentences6 = lists_in_list(sentences6)
sentences7 = lists_in_list(sentences7)
sentences8 = lists_in_list(sentences8)

# todo: double for loop? for sentences in sent_list -> for sentence in sentences

emotions = []
for sentence in sentences:
    message = sentence
    print('MESSAGE: ', message)
    seq = tokenizer.texts_to_sequences(message)
    print('SEQ: ', seq)
    padded = pad_sequences(seq, maxlen=max_seq_len)
    print('PADDED: ', padded)
    pred = model.predict(padded)
    print('PRED: ', pred)
    print('Message: ' + str(message))
    print('Emotion: ', class_names[np.argmax(pred)])
    emotions.append(class_names[np.argmax(pred)])

emotions2 = []
for sentence in sentences2:
    message = sentence
    print('MESSAGE: ', message)
    seq = tokenizer.texts_to_sequences(message)
    print('SEQ: ', seq)
    padded = pad_sequences(seq, maxlen=max_seq_len)
    print('PADDED: ', padded)
    pred = model.predict(padded)
    print('PRED: ', pred)
    print('Message: ' + str(message))
    print('Emotion: ', class_names[np.argmax(pred)])
    emotions2.append(class_names[np.argmax(pred)])

emotions3 = []
for sentence in sentences3:
    message = sentence
    print('MESSAGE: ', message)
    seq = tokenizer.texts_to_sequences(message)
    print('SEQ: ', seq)
    padded = pad_sequences(seq, maxlen=max_seq_len)
    print('PADDED: ', padded)
    pred = model.predict(padded)
    print('PRED: ', pred)
    print('Message: ' + str(message))
    print('Emotion: ', class_names[np.argmax(pred)])
    emotions3.append(class_names[np.argmax(pred)])

emotions4 = []
for sentence in sentences4:
    message = sentence
    print('MESSAGE: ', message)
    seq = tokenizer.texts_to_sequences(message)
    print('SEQ: ', seq)
    padded = pad_sequences(seq, maxlen=max_seq_len)
    print('PADDED: ', padded)
    pred = model.predict(padded)
    print('PRED: ', pred)
    print('Message: ' + str(message))
    print('Emotion: ', class_names[np.argmax(pred)])
    emotions4.append(class_names[np.argmax(pred)])

emotions5 = []
for sentence in sentences5:
    message = sentence
    print('MESSAGE: ', message)
    seq = tokenizer.texts_to_sequences(message)
    print('SEQ: ', seq)
    padded = pad_sequences(seq, maxlen=max_seq_len)
    print('PADDED: ', padded)
    pred = model.predict(padded)
    print('PRED: ', pred)
    print('Message: ' + str(message))
    print('Emotion: ', class_names[np.argmax(pred)])
    emotions5.append(class_names[np.argmax(pred)])

emotions6 = []
for sentence in sentences6:
    message = sentence
    print('MESSAGE: ', message)
    seq = tokenizer.texts_to_sequences(message)
    print('SEQ: ', seq)
    padded = pad_sequences(seq, maxlen=max_seq_len)
    print('PADDED: ', padded)
    pred = model.predict(padded)
    print('PRED: ', pred)
    print('Message: ' + str(message))
    print('Emotion: ', class_names[np.argmax(pred)])
    emotions6.append(class_names[np.argmax(pred)])

emotions7 = []
for sentence in sentences7:
    message = sentence
    print('MESSAGE: ', message)
    seq = tokenizer.texts_to_sequences(message)
    print('SEQ: ', seq)
    padded = pad_sequences(seq, maxlen=max_seq_len)
    print('PADDED: ', padded)
    pred = model.predict(padded)
    print('PRED: ', pred)
    print('Message: ' + str(message))
    print('Emotion: ', class_names[np.argmax(pred)])
    emotions7.append(class_names[np.argmax(pred)])

emotions8 = []
for sentence in sentences8:
    message = sentence
    print('MESSAGE: ', message)
    seq = tokenizer.texts_to_sequences(message)
    print('SEQ: ', seq)
    padded = pad_sequences(seq, maxlen=max_seq_len)
    print('PADDED: ', padded)
    pred = model.predict(padded)
    print('PRED: ', pred)
    print('Message: ' + str(message))
    print('Emotion: ', class_names[np.argmax(pred)])
    emotions8.append(class_names[np.argmax(pred)])

df['Emotion'] = emotions
df2['Emotion'] = emotions2
df3['Emotion'] = emotions3
df4['Emotion'] = emotions4
df5['Emotion'] = emotions5
df6['Emotion'] = emotions6
df7['Emotion'] = emotions7
df8['Emotion'] = emotions8

df.to_csv('/content/drive/MyDrive/p1.csv', sep=',')
df2.to_csv('/content/drive/MyDrive/p2.csv', sep=',')
df3.to_csv('/content/drive/MyDrive/p3.csv', sep=',')
df4.to_csv('/content/drive/MyDrive/p4.csv', sep=',')
df5.to_csv('/content/drive/MyDrive/p5.csv', sep=',')
df6.to_csv('/content/drive/MyDrive/p6.csv', sep=',')
df7.to_csv('/content/drive/MyDrive/p7.csv', sep=',')
df8.to_csv('/content/drive/MyDrive/p8.csv', sep=',')
