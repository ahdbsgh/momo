import pandas as pd
from Korpora import Korpora
import nltk
from konlpy.tag import Mecab
import torch
import torchtext
from torchtext.legacy.data import Field
from nltk.tokenize import TreebankWordTokenizer
from torchtext.legacy.data import TabularDataset
from torchtext.legacy.data import Iterator

token_ko = Mecab()
token_en = TreebankWordTokenizer()

def tokenize_ko(text):
    """
    Tokenizes Korean text from a string into a list of strings (tokens) and reverses it
    """
    return [tok.text for tok in token_ko.morphs(text)][::-1]

def tokenize_en(text):
    """
    Tokenizes English text from a string into a list of strings (tokens)
    """
    return [tok.text for tok in token_en.tokenize(text)]

Korpora.fetch('korean_parallel_koen_news')

corpus = Korpora.load("korean_parallel_koen_news")

ko = corpus.train.texts
en = corpus.train.pairs

# ko = pd.DataFrame(ko)
# en = pd.DataFrame(en)

tok_ko = Field(tokenize = tokenize_ko,
            init_token = '<sos>',
            eos_token = '<eos>',
            lower = False)

tok_en = Field(tokenize = tokenize_en,
            init_token = '<sos>',
            eos_token = '<eos>',
            lower = True)

# print(ko)

print(tok_ko.tokenize(ko))
print(tok_en.tokenize(en))

