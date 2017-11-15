from time import time
import pandas as pd
import numpy as np
from gensim.models import KeyedVectors
import re
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

import itertools
import datetime

from keras.preprocessing.sequence import pad_sequences
from keras.models import Model
from keras.layers import Input, Embedding, LSTM, Merge
import keras.backend as K
from keras.optimizers import Adadelta
from keras.callbacks import ModelCheckpoint
import pickle

# create global vars
loadFlag = 0
vocab_len = 121320
embedding_dim = 300
embeddings = np.load("emb.npy")
max_seq_length = 213
EMBEDDING_FILE = 'GoogleNews-vectors-negative300.bin.gz'
stops = set(stopwords.words('english'))
vocabulary = dict()
inverse_vocabulary = ['<unk>']  # '<unk>' will never be used, it is only a placeholder for the [0, 0, ....0] embedding
word2vec = None
with open("vocab.txt", "rb") as fp:
    vocabulary = pickle.load(fp)

with open("inverseVocab.txt", "rb") as fp1:
    inv = pickle.load(fp1)
    inverse_vocabulary = inverse_vocabulary + inv


#model vars
n_hidden = 50
gradient_clipping_norm = 1.25
batch_size = 128
n_epoch = 10

def exponent_neg_manhattan_distance(left, right):
    ''' Helper function for the similarity estimate of the LSTMs outputs'''
    return K.exp(-K.sum(K.abs(left-right), axis=1, keepdims=True))

# The visible layer
left_input = Input(shape=(max_seq_length,), dtype='int32')
right_input = Input(shape=(max_seq_length,), dtype='int32')

embedding_layer = Embedding(len(embeddings), embedding_dim, weights=[embeddings], input_length=max_seq_length, trainable=False)

# Embedded version of the inputs
encoded_left = embedding_layer(left_input)
encoded_right = embedding_layer(right_input)

# Since this is a siamese network, both sides share the same LSTM
shared_lstm = LSTM(n_hidden)

left_output = shared_lstm(encoded_left)
right_output = shared_lstm(encoded_right)

# Calculates the distance as defined by the MaLSTM model
malstm_distance = Merge(mode=lambda x: exponent_neg_manhattan_distance(x[0], x[1]), output_shape=lambda x: (x[0][0], 1))([left_output, right_output])
malstm = Model([left_input, right_input], [malstm_distance])




def text_to_word_list(text):
    ''' Pre process and convert texts to a list of words '''
    text = str(text)
    text = text.lower()

    # Clean the text
    text = re.sub(r"[^A-Za-z0-9^,!.\/'+-=]", " ", text)
    text = re.sub(r"what's", "what is ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"can't", "cannot ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub(r",", " ", text)
    text = re.sub(r"\.", " ", text)
    text = re.sub(r"!", " ! ", text)
    text = re.sub(r"\/", " ", text)
    text = re.sub(r"\^", " ^ ", text)
    text = re.sub(r"\+", " + ", text)
    text = re.sub(r"\-", " - ", text)
    text = re.sub(r"\=", " = ", text)
    text = re.sub(r"'", " ", text)
    text = re.sub(r"(\d+)(k)", r"\g<1>000", text)
    text = re.sub(r":", " : ", text)
    text = re.sub(r" e g ", " eg ", text)
    text = re.sub(r" b g ", " bg ", text)
    text = re.sub(r" u s ", " american ", text)
    text = re.sub(r"\0s", "0", text)
    text = re.sub(r" 9 11 ", "911", text)
    text = re.sub(r"e - mail", "email", text)
    text = re.sub(r"j k", "jk", text)
    text = re.sub(r"\s{2,}", " ", text)

    text = text.split()

    return text

def getEmbdPair(question_pair):
    res = []
    for question in question_pair:
        qtn = []
        for word in text_to_word_list(question):
            if word in stops and word not in word2vec.vocab:
                continue
            if word not in vocabulary:
                vocabulary[word] = len(inverse_vocabulary)
                qtn.append(len(inverse_vocabulary))
                inverse_vocabulary.append(word)
            else:
                qtn.append(vocabulary[word])
        res.append(qtn)
    return res #return pair of embeddings

def ZeroPad(qPair):
    resPair = []
    resPair.append(pad_sequences(qPair, maxlen=max_seq_length))
    return resPair

def load():
    global loadFlag
    if loadFlag == 0:
        global malstm
        global word2vec
        word2vec = KeyedVectors.load_word2vec_format(EMBEDDING_FILE, binary=True)
        malstm.load_weights("model/sem.h5")
        print "loading complete"
        loadFlag = 1
    else:
        print "already loaded"

    #return "Model loaded"

def calc(s1, s2):
    if loadFlag == 0:
        print "load model first"
        return
    question_pair = [s1, s2]
    emb = ZeroPad(getEmbdPair(question_pair))
    arg = [np.asarray([emb[0][0]]), np.asarray([emb[0][1]])]
    pred = malstm.predict(arg)
    # print pred
    return float(pred[0][0].item())


