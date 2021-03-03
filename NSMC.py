from konlpy.tag import Kkma
from konlpy.tag import Komoran
from konlpy.tag import Hannanum
from konlpy.tag import Mecab
from konlpy.tag import Okt
import pandas as pd
from Korpora import Korpora

# 형태소 분석을 위한 객체 생성.
kkma = Kkma()
komoran = Komoran()
hannanum = Hannanum()
mecab = Mecab()
okt = Okt()

text ="안녕 나는 윤호라고해"


# print(kkma.pos(text))
# print(komoran.pos(text))
# print(hannanum.pos(text))
# print(okt.pos(text))
# print(mecab.pos(text))

corpus = Korpora.load("nsmc")


train_data = pd.read_table('ratings_train.txt')
test_data = pd.read_table('ratings_test.txt')