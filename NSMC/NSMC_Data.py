import pandas as pd
import torchtext
from torchtext import data
from konlpy.tag import Mecab
import torchtext.legacy as torchtext
from torchtext.legacy.data import TabularDataset
from torchtext.legacy.data import Iterator



tokenizer = Mecab()


train_data = pd.read_table(r'ratings_train.txt')
test_data = pd.read_table(r'ratings_test.txt')


train_data = train_data.drop('id', axis=1)
test_data = test_data.drop('id', axis=1)
# print(train_data.head(5))
# print(test_data.head(5))
ID = torchtext.data.Field(sequential = False,
                use_vocab = False) # 실제 사용은 하지 않을 예정

TEXT = torchtext.data.Field(sequential=True,
                  use_vocab=True,
                  tokenize=tokenizer.morphs, # 토크나이저로는 Mecab 사용.
                  lower=True,
                  batch_first=True,
                  fix_length=20)

LABEL = torchtext.data.Field(sequential=False,
                   use_vocab=False,
                   is_target=True)

train_data, test_data = TabularDataset.splits(
        path='.', train='ratings_train.txt', test='ratings_test.txt', format='tsv',
        fields=[('id', ID), ('text', TEXT), ('label', LABEL)], skip_header=True)

# print('훈련 샘플의 개수 : {}'.format(len(train_data)))
# print('테스트 샘플의 개수 : {}'.format(len(test_data)))

# print(vars(train_data[0]))

TEXT.build_vocab(train_data, min_freq=10, max_size=10000)

# print('단어 집합의 크기 : {}'.format(len(TEXT.vocab)))

# print(TEXT.vocab.stoi)

# print(TEXT.vocab.stoi)

batch_size = 5

train_loader = Iterator(dataset=train_data, batch_size = batch_size)
test_loader = Iterator(dataset=test_data, batch_size = batch_size)


print('훈련 데이터의 미니 배치 수 : {}'.format(len(train_loader)))
print('테스트 데이터의 미니 배치 수 : {}'.format(len(test_loader)))

batch = next(iter(train_loader)) # 첫번째 미니배치
print(batch.text)