# This code is inspired by the article "Emotion Recognition using Text", written by Abhinav Kumar

import pandas as pd
import numpy as np
import re
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from keras.models import load_model
import urllib.request
import zipfile
import os
from keras.models import Sequential
from keras.layers import Embedding,Bidirectional,LSTM,GRU,Dense
import nltk
from nltk.tokenize import word_tokenize
import warnings
import tensorflow as tf
nltk.download('punkt')
warnings.filterwarnings('ignore')
