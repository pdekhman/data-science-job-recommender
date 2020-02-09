import pandas as pd
import numpy as np 


import time, os
import pickle
from collections import Counter
from tqdm import tqdm


import re
import string

import nltk
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import WordNetLemmatizer

import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from collections import Counter
from spacy.lang.en import English
from spacy import displacy
nlp = spacy.load("en_core_web_sm")


from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA


import matplotlib.pyplot as plt
import seaborn as sns


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_rows', 500)

def load_clean_nlp(path,data,text_column):
    data = open(path+data,"rb")
    listings = pickle.load(data)
    df = pd.DataFrame(listings)
    df[text_column]  =[' '.join(i) for i in df[text_column]]
    df.drop_duplicates(subset = [text_column], keep ='first',inplace=True)
    df.reset_index(drop=True,inplace=True)

    return df

def spacy_tagging_demo (text):
    mytokens = nlp(text)

    tokens_list = []
    for token in mytokens:
        mytoken = {}
        mytoken['text'] = token.text
        mytoken['lemma'] = token.lemma_
        mytoken['POS'] = token.pos_
        mytoken['tag'] = token.tag_
        mytoken['dep'] = token.dep_
        mytoken['shape'] = token.shape_
        mytoken['Is_Alpha?'] = token.is_alpha
        mytoken['Is_stop?'] = token.is_stop
        mytoken['Is_punct?'] = token.is_punct
        mytoken['Is_digit?'] = token.is_digit
        tokens_list.append(mytoken)

    tokens_df = pd.DataFrame(tokens_list)
    return tokens_df


new_stop_words = ['experience','years','work','learning','data','science','race',
'gender','religion','origin','sexual','orientation','color','status',
'national','statistics','team','new','customer','help','opportunity',
'business','must','position','education','employment','please',
'working','applicant','best','disability','job','using','may',
'strong','etc','building','related','support','including'
 ,'skills','technical','across','time','tools','analytics','development'
,'understanding','fortune','workplace','company','report','required','requirement',
'health','year','veteran','provide','e.g.','ability','amazon','united','states','degree','bachelors',
'qualifications', 'preferred', 'scientist', 'bachelor', 'responsibilities', 'engineer', 'group', 'equal', '000', 'minimum',
'san','san francisco', 'francisco', 'insurance', 'dental', 'vision', 'program', 'medical', 'management', 'dental', 'vision'
     ,'information','masters','applied','information','knowledge']


def text_process(text,extra_stopwords,punctuation):
    punctuation = string.punctuation
    final_stopwords =  list(STOP_WORDS)+new_stop_words
    if text !=None:
        mytokens = [word for word in text if word.is_digit != True and word.is_punct != True]
        mytokens = [word for word in mytokens if word.pos_ not in ['VERB','ADV','ADJ','ADP','DET','NOUN']]
        mytokens = [word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_ for word in mytokens]
        mytokens = [word for word in mytokens if word not in final_stopwords and word not in punctuation and '@' not in word and 'http' not in word]
        mytokens = " ".join([i for i in mytokens])
        return mytokens
    else:
        return ""

def display_topics(model, feature_names, no_top_words, topic_names=None):
    for ix, topic in enumerate(model.components_):
        if not topic_names or not topic_names[ix]:
            print("\nTopic ", ix)
        else:
            print("\nTopic: '",topic_names[ix],"'")
        print(", ".join([feature_names[i] for i in topic.argsort()[:-no_top_words - 1:-1]]))
