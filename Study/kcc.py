import pandas as pd
from Korpora import Korpora
import nltk
from konlpy.tag import Mecab
import torch
import torchtext
from torchtext.data import Field
from nltk.tokenize import word_tokenize
from nltk.tokenize import TreebankWordTokenizer
from nltk.tag import pos_tag
from torchtext.data import TabularDataset
from torchtext.data import Iterator

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
#################################################################################
# Korpora.fetch('korean_parallel_koen_news')
#
# corpus = Korpora.load("korean_parallel_koen_news")
#
# print(corpus)
# train_df = corpus.train
# test_df = corpus.test
# dev_df = corpus.dev
#
# train_df = pd.DataFrame(train_df)
# test_df = pd.DataFrame(test_df)
# dev_df = pd.DataFrame(dev_df)
#
# print(train_df)
#
# train_df.to_csv('train_df.csv')
# test_df.to_csv('test_df.csv')
# dev_df.to_csv('dev_df.csv')          ## 데이터 CSV파일로 변환후 사용

#############################################################
train_df = pd.read_csv('data/train_df.csv')
test_df = pd.read_csv('data/test_df.csv')
dev_df = pd.read_csv('data/dev_df.csv')

# print(train_df)
# print(train_df['text'])
# print(train_df['pair'])

train_kor_df = train_df['text']
train_eng_df = train_df['pair']

# print(train_kor_df)
# print(train_eng_df)


ko_dic = []
for ko in train_kor_df:
    tmp = []
    tmp = token_ko.pos(ko)

    ko_dic.append(tmp)

print(ko_dic[1])

en_dic = []
for en in train_eng_df:
    tmp = []
    tmp = pos_tag(token_en.tokenize(en))

    en_dic.append(tmp)

print(en_dic[1])



# id = Field(sequential = False,
#            use_vocab = False) # 실제 사용은 하지 않을 예정

# kor = Field(sequential = True,
#             tokenize = token_ko.pos,
#             init_token = '<sos>',
#             eos_token = '<eos>',
#             batch_first=True,
#             use_vocab=True,
#             )

# eng = Field(sequential = True,
#             tokenize = pos_tag(token_en.tokenize),
#             init_token = '<sos>',
#             eos_token = '<eos>',
#             batch_first=True,
#             use_vocab=True,
#             lower = True)
# #
# train_data, test_data = TabularDataset.splits(
#         path='.', train='data/train_df.csv', test='data/test_df.csv', format='csv',
#         fields=[('id', id ), ('text', kor), ('pair', eng)],skip_header=True)

# print('훈련 샘플의 개수 : {}'.format(len(train_data)))
# print('테스트 샘플의 개수 : {}'.format(len(test_data)))

# # print(vars(train_data[0]))
# print(vars(train_data[0]))

# kor.build_vocab(train_data, min_freq=10, max_size=10000)
# eng.build_vocab(train_data, min_freq=10, max_size=10000)

# print('단어 집합의 크기 : {}'.format(len(kor.vocab)))
# print('단어 집합의 크기 : {}'.format(len(eng.vocab)))

# print(kor.vocab.stoi)
# print(eng.vocab.stoi)

# batch_size = 5

# train_loader = Iterator(dataset=train_data, batch_size = batch_size)
# test_loader = Iterator(dataset=test_data, batch_size = batch_size)

# print(train_loader.dataset)

# # print('훈련 데이터의 미니 배치 수 : {}'.format(len(train_loader)))
# # print('테스트 데이터의 미니 배치 수 : {}'.format(len(test_loader)))

# batch = next(iter(train_loader)) # 첫번째 미니배치
# print(batch.text)

# #todo: 데이터 loader을 만들고 있다. 더 확실하게 만들어보자.

# 이건 Passing 이 아니라 POS Tagging 임
# 우리가 이번에 해야할것은 Passing 


