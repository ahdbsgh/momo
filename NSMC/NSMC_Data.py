import pandas as pd
import torchtext
from torchtext import data
from konlpy.tag import Mecab
from torchtext.data import TabularDataset


tokenizer = Mecab()

train_df = pd.read_table(r'C:\Users\Gachon\WorkSpace\momo\NSMC\ratings_train.txt')
test_df = pd.read_table(r'C:\Users\Gachon\WorkSpace\momo\NSMC\ratings_test.txt')


# train_data = train_data.drop('id', axis=1)
# test_data = test_data.drop('id', axis=1)
# print(train_df.head(5))
# print(test_df.head(5))
ID = data.Field(sequential = False,
                use_vocab = False) # 실제 사용은 하지 않을 예정

TEXT = data.Field(sequential=True,
                  use_vocab=True,
                  tokenize=tokenizer.morphs, # 토크나이저로는 Mecab 사용.
                  lower=True,
                  batch_first=True,
                  fix_length=20)

LABEL = data.Field(sequential=False,
                   use_vocab=False,
                   is_target=True)

train_data, test_data = TabularDataset.splits(
        path='.', train='ratings_train.txt', test='ratings_test.txt', format='tsv',
        fields=[('id', ID), ('text', TEXT), ('label', LABEL)], skip_header=True)

print('훈련 샘플의 개수 : {}'.format(len(train_data)))
print('테스트 샘플의 개수 : {}'.format(len(test_data)))
