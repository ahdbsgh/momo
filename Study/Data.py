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

# def tokenize_ko(text):
#     """
#     Tokenizes Korean text from a string into a list of strings (tokens) and reverses it
#     """
#     return [tok.text for tok in token_ko.morphs(text)][::-1]
#
# def tokenize_en(text):
#     """
#     Tokenizes English text from a string into a list of strings (tokens)
#     """
#     return [tok.text for tok in token_en.tokenize(text)]

# Korpora.fetch('korean_parallel_koen_news')
#
# corpus = Korpora.load("korean_parallel_koen_news")

# print(corpus)
# ko = corpus.train.texts
# en = corpus.train.pairs

# ko = pd.DataFrame(ko)
# en = pd.DataFrame(en)



# kor = Field(tokenize = token_ko.morphs,
#             init_token = '<sos>',
#             eos_token = '<eos>',
#             lower = False)
#
# eng = Field(tokenize = token_en.tokenize,
#             init_token = '<sos>',
#             eos_token = '<eos>',
#             lower = True)
# #
# # train_data, test_data = TabularDataset.splits(
# #         path='.', train=corpus.train, test=corpus.test, format='tsv',
# #         fields=[('kor', kor), ('eng', eng)])
# train_data, valid_data, test_data = corpus.splits(fields = (kor, eng))


# print(ko)
#
# print(token_ko.morphs(ko))
# print(token_en.tokenize(en))

# test = "안녕 나는 윤호라고 해"
#
# print(token_ko.morphs(test))

from hanspell import spell_checker
result = spell_checker.check('안녕? 나는 모윤호라고해 나는 한국인이야. 밥은먹었니?.')
result.as_dict()  # dict로 출력
print(result)

#todo: torchtext 로 사용하니 안된다. 다른 SOS, EOS를 넣는 방법을 생각해보자


